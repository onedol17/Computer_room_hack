
void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    
  }

}

void short_sign() {
  digitalWrite(13, High);//디지털 핀 13 끄기
  delay(500);//1초 기다리기
  digitalWrite(13, Low)
}

void long_sign() {
  digitalWrite(13, High);//디지털 핀 13 끄기
  delay(2000);//1초 기다리기
  digitalWrite(13, Low)
}