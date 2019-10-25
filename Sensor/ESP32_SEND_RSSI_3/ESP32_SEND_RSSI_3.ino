#include <BLEDevice.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define ADDRESS "ff:ff:c2:0f:ed:8d" 

const char* ssid = "Nokia 3";
const char* password = "hasbi1202";

BLEScan* pBLEScan;
boolean found = false;
int rssi = -120;
String mac;
StaticJsonDocument<200> json;

//Fungsi callback scan
class MyAdvertisedDeviceCallbacks: public BLEAdvertisedDeviceCallbacks
{
    void onResult(BLEAdvertisedDevice advertisedDevice) {
      
      //fungsi untuk mendapatkan RSSI device iTAG
      if (strcmp(advertisedDevice.getAddress().toString().c_str(), ADDRESS) == 0) {
        rssi = advertisedDevice.getRSSI();
        advertisedDevice.getScan()->stop();
      }
    }
};

void setup()
{
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) { //Check for the connection
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  Serial.println("Connected to the WiFi network");

  Serial.println(WiFi.macAddress());
  mac = String(WiFi.macAddress());

  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan();
  pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
  pBLEScan->setActiveScan(true);

}

void loop()
{
  pBLEScan->start(1);
  HTTPClient http;

  http.begin("http://192.168.43.242:8080/");  //Menentukan tujuan pengiriman data
  http.addHeader("Content-Type", "application/json");  //menentukan header http
  http.setTimeout(500);
  String postMessage;

  json["mac"] = mac;
  json["rssi"] = rssi;

  serializeJson(json, postMessage);

  int httpResponseCode = http.POST(postMessage); //Mengirim data POST

  http.end();

  Serial.print("RSSI: ");
  Serial.println(rssi);

  pBLEScan->clearResults();
  json.JsonDocument::clear();
  rssi = -120;
}
