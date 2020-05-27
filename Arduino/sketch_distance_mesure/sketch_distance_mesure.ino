/* Utilisation du capteur Ultrason HC-SR04 */
 
// définition des broches utilisées 
int trig = 11; 
int echo = 12; 
long lecture_echo; 
long cm;
 
void setup() 
{ 
  pinMode(trig, OUTPUT);  
  pinMode(echo, INPUT); 
  Serial.begin(9600); 
}
 
void loop() 
{ 
  long duree, distance;
  digitalWrite(trig, LOW); 
  delayMicroseconds(2); // envoi d'une impulsion sur trig de 10 microsecondes
  digitalWrite(trig, HIGH); 
  delayMicroseconds(10); //Trig envois pendant 10ms 
  digitalWrite(trig, LOW); 
   
  duree = pulseIn(echo, HIGH); 
  distance = duree*340/(2*10000); 
  Serial.print("Distance en cm : "); 
  Serial.print(duree);
  Serial.print(" ");
  Serial.println(distance); 
  delay(100); 
}
