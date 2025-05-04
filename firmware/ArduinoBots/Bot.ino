#include <ArduinoBLE.h>
#include "config.h"

int energy = MAX_ENERGY;

void setup() {
  Serial.begin(9600);
  BLE.begin();
  BLE.setLocalName(BLE_DEVICE_NAME);
  BLE.advertise();
  Serial.printf("Bot %d initialized. BLE name: %s\n", BOT_ID, BLE_DEVICE_NAME);
}

void loop() {
  // Simulate power drain & recharge near inductive pad
  if (digitalRead(A0) == HIGH) energy = min(MAX_ENERGY, energy + 1);
  else energy = max(0, energy - 1);

  // Advertise battery status over BLE
  BLEDevice central = BLE.central();
  if (central) {
    BLECharacteristic statusChar("180F", "2A19"); // battery service/char
    statusChar.writeValue((uint8_t)energy);
  }

  // Simple formation mode trigger (e.g. magnetic lock)
  if (energy > 50 && digitalRead(2) == HIGH) {
    Serial.println("Formation mode engaged!");
    // TODO: rotate servos or lock magnets
  }

  delay(100);
}
