const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  while (!Serial) {
    // Wait for serial connection
  }
  Serial.println("Arduino ready for LED control.");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // Remove any extra whitespace

    if (command == "on") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED is ON");
    } else if (command == "off") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED is OFF");
    }
  }
}
