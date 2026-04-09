/*
  esp8266_servo_mqtt.ino

  ESP8266 servo control over MQTT.
  Subscribes to a command topic and performs a simple wave motion.

  Update these before uploading:
  - WIFI_SSID
  - WIFI_PASSWORD
  - MQTT_BROKER
  - DEVICE_TOPIC_CMD
  - DEVICE_TOPIC_RESP
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>

const char* WIFI_SSID = "ESP32-Hub";
const char* WIFI_PASSWORD = "Tryptol1n3!";
const char* MQTT_BROKER = "192.168.4.1";

const char* DEVICE_NAME = "esp8266_servo_1";
const char* DEVICE_TOPIC_CMD = "servo/esp8266/cmd";
const char* DEVICE_TOPIC_RESP = "servo/esp8266/response";

const int SERVO_PIN = 2;   // D4 / GPIO2 in your earlier setup

WiFiClient wifiClient;
PubSubClient client(wifiClient);
Servo myServo;

void connectWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnectMQTT() {
  while (!client.connected()) {
    if (client.connect(DEVICE_NAME)) {
      client.subscribe(DEVICE_TOPIC_CMD);
      client.publish(DEVICE_TOPIC_RESP, "ESP8266 connected");
    } else {
      delay(1000);
    }
  }
}

void doWave() {
  for (int i = 0; i < 3; i++) {
    myServo.write(40);
    delay(300);
    myServo.write(120);
    delay(300);
  }
  myServo.write(90);
}

void callback(char* topic, byte* payload, unsigned int length) {
  String msg = "";
  for (unsigned int i = 0; i < length; i++) {
    msg += (char)payload[i];
  }

  if (msg == "wave") {
    doWave();
    client.publish(DEVICE_TOPIC_RESP, "ESP8266 wave complete");
  } else if (msg == "center") {
    myServo.write(90);
    client.publish(DEVICE_TOPIC_RESP, "ESP8266 centered");
  } else {
    client.publish(DEVICE_TOPIC_RESP, "ESP8266 unknown command");
  }
}

void setup() {
  myServo.attach(SERVO_PIN);
  myServo.write(90);

  connectWiFi();
  client.setServer(MQTT_BROKER, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();
}
