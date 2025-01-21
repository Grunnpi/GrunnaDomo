/*
   pH + ORP/Redox + temperature multifunction
*/
// lib 1-wire for temperature
#include <OneWire.h>
#include <DallasTemperature.h>

#define myVersion "v1.0 - 2020-06-12"

// Arduino pin
#define pH_SensorPin A1               // pH meter Analog output to Arduino Analog Input 0
#define ORP_Pin A1                    // orp meter output,connect to Arduino controller ADC pin
#define ONE_WIRE_BUS 4                // Data wire is conntec to the Arduino digital pin 4


#define PH_ENABLED
//#define ORP_ENABLED
//#define TEMPERATURE_ENABLED

/* ******************************************************************************* */
/* general variables */
/* ******************************************************************************* */
#define printInterval 5000           // write values every 10000 milliseconds
#define samplingInterval 10           // sample values every 10 milliseconds
#define arrayLenth 40                 // sample size

/* ******************************************************************************* */
/* tempaterature related */
/* ******************************************************************************* */

#ifdef TEMPERATURE_ENABLED
  // temparature DS18B20 init
  OneWire oneWire(ONE_WIRE_BUS);        // Setup a oneWire instance to communicate with any OneWire devices
  DallasTemperature sensors(&oneWire);  // Pass our oneWire reference to Dallas Temperature sensor 
  int temperature_Array[arrayLenth];             // store the average value of the sensor feedback
  int temperature_ArrayIndex=0;
#endif

/* ******************************************************************************* */
/* pH related */
/* ******************************************************************************* */
#ifdef PH_ENABLED
  // probe calibration
//  #define pH_Offset 3.73                // deviation compensation
  #define pH_Offset 6.74                // deviation compensation
  
  // ph probe stuff
  int pH_Array[arrayLenth];             // store the average value of the sensor feedback
  int pH_ArrayIndex=0;
#endif

/* ******************************************************************************* */
/* ORP/Redux related */
/* ******************************************************************************* */
#ifdef ORP_ENABLED
  // probe calibration
  #define ORP_system_voltage 5.00       // system voltage
  
  #define ORP_OFFSET -410               // zero drift voltage
  
  // orp/redux stuff
  int ORP_Array[arrayLenth];
  int ORP_ArrayIndex=0;
#endif


// average
double avergearray(int* arr, int number){
  double temp;

  // sort array
  for(int i=0;i<number;i++) {
    for(int j=i+1;j<10;j++) {
      if(arr[i]>arr[j]) {
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
      }
    }
  }

  double avgValue=0;
  for(int i=2;i<number - 2;i++) {
    avgValue+=arr[i];
  }
  avgValue = (avgValue / (number-2));
  return avgValue;
}    

//general formula returning average
double avergearray2(int* arr, int number){
        int i;
        int max,min;
        double avg;
        long amount=0;
        if(number<=0) {
                printf("Error number for the array average!/n");
                return 0;
        }
        if(number<5) { //less than 5, calculated directly statistics
                for(i=0; i<number; i++) {
                        amount+=arr[i];
                }
                avg = amount/number;
                return avg;
        }else{
                if(arr[0]<arr[1]) {
                        min = arr[0]; max=arr[1];
                }
                else{
                        min=arr[1]; max=arr[0];
                }
                for(i=2; i<number; i++) {
                        if(arr[i]<min) {
                                amount+=min;
                                min=arr[i];
                        }else {
                                if(arr[i]>max) {
                                        amount+=max;
                                        max=arr[i];
                                }else{
                                        amount+=arr[i];
                                }
                        }
                }
                avg = (double)amount/(number-2);
        }
        return avg;
}

// init
void setup(void)
{
    Serial.begin(9600);
    Serial.print("Sensor[");

    #ifdef ORP_ENABLED
      Serial.print("ORP/redox][");
    #endif

    #ifdef PH_ENABLED
      Serial.print("pH][");
    #endif

    #ifdef TEMPERATURE_ENABLED
      Serial.print("Temperature][");
    #endif

    Serial.print(myVersion);
    Serial.println("]");
    
    while (!Serial) {
      ; // wait for serial port to connect. Needed for native USB port only
    }

    #ifdef TEMPERATURE_ENABLED
      // init temperature
      sensors.begin();
    #endif
        
    Serial.println("initialization done.");
}

// main loop
void loop(void)
{
    static unsigned long measure_samplingTime = millis();
    static unsigned long GENERAL_printTime = millis();
    #ifdef PH_ENABLED
      static float pH_Value;
      static float pH_voltage;
    #endif
    #ifdef ORP_ENABLED    
      double ORP_Value;
    #endif
    #ifdef TEMPERATURE_ENABLED
      static float temperature_Value;
       
    #endif
    
    if( ( millis() - measure_samplingTime ) > samplingInterval) //read an analog value every 20ms
    {
        #ifdef PH_ENABLED
          // read value & store in array
          pH_Array[pH_ArrayIndex++]   = analogRead(pH_SensorPin);


          pH_voltage = pH_Array[pH_ArrayIndex] * 5.0 / 1024 / 6;
          pH_Value = 3.5 * pH_voltage + pH_Offset;
          Serial.print("pH[");
          Serial.print(pH_Value,2);
          Serial.println("]");
          
           // beware of out of bound
          if(pH_ArrayIndex==arrayLenth) {
            pH_ArrayIndex=0;
          }
           
          // average value
          pH_voltage = avergearray(pH_Array, arrayLenth) * 5.0 / 1024 / 6;
          pH_Value = 3.5 * pH_voltage + pH_Offset;
          //pH_Value = -5.70 * pH_voltage + pH_Offset;

          
        #endif
        
        #ifdef ORP_ENABLED
          ORP_Array[ORP_ArrayIndex++] = analogRead(ORP_Pin); 
          
          if (ORP_ArrayIndex==arrayLenth) {
            ORP_ArrayIndex=0;
          }
          
          ORP_Value=((30*(double) ORP_system_voltage * 1000) - (75*avergearray(ORP_Array, arrayLenth)* ORP_system_voltage *1000/1024)) / 75 - ORP_OFFSET;           
        #endif

        #ifdef TEMPERATURE_ENABLED
          sensors.requestTemperatures(); // Call sensors.requestTemperatures() to issue a global temperature and Requests to all devices on the bus
          temperature_Array[temperature_ArrayIndex++] = sensors.getTempCByIndex(0);

          if (temperature_ArrayIndex==arrayLenth) {
            temperature_ArrayIndex=0;
          }

          temperature_Value = avergearray(temperature_Array, arrayLenth);
        #endif
                  
        measure_samplingTime = millis() + 10;
    }
    
    if(millis() - GENERAL_printTime >= printInterval) //print to serial monitor and write to file
    {
        Serial.print("[");
        Serial.print(millis()/1000);
        Serial.print(" sec] ");

        #ifdef ORP_ENABLED
          Serial.print(", ORP/redox[");
          Serial.print((int)ORP_Value);
          Serial.print(" mV]");
        #endif

        #ifdef PH_ENABLED
          Serial.print(", pH[");
          Serial.print(pH_Value,2);
          Serial.print("]");
        #endif

        #ifdef TEMPERATURE_ENABLED
          Serial.print(", C°[");
          Serial.print(temperature_Value,2);
          Serial.print("]");
        #endif
        
        Serial.println("");
        GENERAL_printTime=millis();             
    }
}
