// Home Automation System 
// Snehesh Thalapaneni
void setup() { 
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  
} 
void loop() { 
char light='L';
char fan='F';
char alarm='A';
char data;
while(Serial.available() > 0) { 
data=Serial.read();
if (data==light) { 
  digitalWrite(13,HIGH);
  delay(100);
  digitalWrite(13,LOW);
  delay(100);
}
else if(data==fan) { 
  digitalWrite(13,HIGH);
  delay(3000);
  digitalWrite(13,LOW);
  delay(3000);
}
else if(data==alarm) { 
  digitalWrite(13,HIGH);
  delay(10000);
  digitalWrite(13,LOW);
  delay(10000);
}
else {
  digitalWrite(13,LOW);
  delay(10);
}
}
}
