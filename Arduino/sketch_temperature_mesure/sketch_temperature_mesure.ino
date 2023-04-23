/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
  Based on the Dallas Temperature Library example
*********/

#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is conntec to the Arduino digital pin 4
#define ONE_WIRE_BUS 4

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);

unsigned long previousMillis = 0;//variable delay sans arrêt du programme
const long interval = 1000;// variable delay sans arrêt du programme qui prevoit une lecture de 1 seconde par mesure
DeviceAddress sensorDeviceAddress; //Vérifie la compatibilité des capteurs avec la librairie

void setup(void)
{
  // Start serial communication for debugging purposes
  Serial.begin(9600);
  // Start up the library
  sensors.begin();
  sensors.getAddress(sensorDeviceAddress, 0); //Adresse de la sonde à 0
//  sensors.setResolution(sensorDeviceAddress, 12); //Résolutions
 
  Serial.println("Bienvenue sur les tutoriels de IHM-3D");
 
  delay (2000);
}

void loop(void){ 



  
  // Call sensors.requestTemperatures() to issue a global temperature and Requests to all devices on the bus
  sensors.requestTemperatures(); 
  
  Serial.print("POUET Celsius temperature: ");
  // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire
  Serial.print(sensors.getTempCByIndex(0)); 
  Serial.print(" - Fahrenheit temperature: ");
  Serial.println(sensors.getTempFByIndex(0));
  delay(1000);
}
