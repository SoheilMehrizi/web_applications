const int pin1 = 7;

void setup() {
    Serial.begin(115200);
    pinMode(pin1, OUTPUT);
    digitalWrite(pin1, LOW);

    Serial.println("Serial communication started. Ready to receive commands.");
}

void handleSerialCommand(const String& command) {
    if (command == "activate") {
        digitalWrite(pin1, HIGH);
        delay(5000);
        digitalWrite(pin1, LOW);
        Serial.println("Pin 1 activated for 5 seconds");
    } else {
        Serial.println("Invalid command");
    }
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();  
        handleSerialCommand(command);
    }
}
