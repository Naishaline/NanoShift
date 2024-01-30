int yAxis = A2;
int xAxis = A0;

int yVal = 0;
int xVal = 0;

void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {
  yVal = analogRead(yAxis);
  xVal = analogRead(xAxis);
  Serial.print(xVal);
  Serial.print("|");
  Serial.println(yVal);
}