#include <DHT11.h>
const int sensorPin = A0; // Analog pin connected to sensor's Signal pin
float vout = 0.0;
float vin = 0.0;
const float voltageDividerFactor = 5.0;
DHT11 dht11(2);

void setup() {
    // Initialize serial communication to allow debugging and data readout using a baud rate of 9600 bps.
    Serial.begin(9600);
}

void loop() {
        // put your main code here, to run repeatedly:
    int time=millis()/1000;
    int sensorValue = analogRead(sensorPin);
    vout = (sensorValue * 5.0) / 1023.0;
    vin = vout * voltageDividerFactor;
    float temp=dht11.readTemperature();
    Serial.print(temp);
    Serial.print(",");
    Serial.println(vin);
    delay(500);
}
