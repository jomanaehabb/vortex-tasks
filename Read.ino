const int buttonPin = 2;
int buttonState = 0;
int lastButtonState = 0;

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  while (!Serial) {
    // Wait for serial connection
  }
  Serial.println("Arduino ready to send button state.");
}

void loop() {
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == HIGH) {
        Serial.println("Button Pressed");
      } else {
        Serial.println("Button Released");
      }
    }
  }
  lastButtonState = reading;
}
