float calibration = 2.47; //change this value to calibrate
const int analogInPin = A1; 
int sensorValue = 0; 
unsigned long int avgValue; 
float b;
int buf[10],temp;
void setup() {
 Serial.begin(9600);
 pinMode(analogInPin,OUTPUT);  
}
 
void loop() {
 for(int i=0;i<10;i++) 
 { 
 buf[i]=analogRead(analogInPin);
 delay(30);
 }
 for(int i=0;i<9;i++)
 {
 for(int j=i+1;j<10;j++)
 {
 if(buf[i]>buf[j])
 {
 temp=buf[i];
 buf[i]=buf[j];
 buf[j]=temp;
 }
 }
 }
 avgValue=0;
 for(int i=2;i<8;i++)
 avgValue+=buf[i];
 float pHVol=(float)avgValue*5.0/1024/6;
 float phValue = 3.5 * pHVol + calibration;
 Serial.print("sensor = ");
 Serial.println(phValue);

  digitalWrite(analogInPin, HIGH);       
  delay(800);
  digitalWrite(analogInPin, LOW); 
 
 //delay(500);
}
