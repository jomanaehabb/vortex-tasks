const int trigPin = 9;
const int echoPin = 10;
const int buzzerPin = 3;
const int potPin = A0;

const float speedOfSound = 0.034;

void setup() {
  // Initialize serial monitor
  Serial.begin(9600);
  
  // Set up pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Get distance from ultrasonic sensor
  float distance = getDistance();

  // Print the distance to the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Read potentiometer value and map it to a range of distances
  int potValue = analogRead(potPin);
  float thresholdDistance = map(potValue, 0, 1023, 5, 50);  // Adjust this range as needed

  // Print threshold to Serial Monitor
  Serial.print("Threshold Distance: ");
  Serial.print(thresholdDistance);
  Serial.println(" cm");

  // Check if distance is less than threshold and sound buzzer if true
  if (distance < thresholdDistance) {
    digitalWrite(buzzerPin, HIGH);  // Turn buzzer on
  } else {
    digitalWrite(buzzerPin, LOW);   // Turn buzzer off
  }

  // Small delay for stability
  delay(200);
}

// Function to calculate distance using ultrasonic sensor
float getDistance() {
  // Clear the trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Send a 10µs pulse to the trigger pin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echo pin and calculate distance
  long duration = pulseIn(echoPin, HIGH);
  float distance = (duration * speedOfSound) / 2; // Divide by 2 for round trip
  
  return distance;
}
