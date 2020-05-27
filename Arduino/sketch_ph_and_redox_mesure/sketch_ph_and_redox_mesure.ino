/*
   pH and ORP measurements on Arduino
 */

//pH and ORP variables
#define samplingInterval 10       //sample values every 10 milliseconds
#define pH_SensorPin A0           //pH meter Analog output to Arduino Analog Input 0
#define ORP_Pin A1                 //orp meter output,connect to Arduino controller ADC pin

#define pH_Offset 3.73            //deviation compensation
#define ORP_OFFSET -410             //zero drift voltage

#define arrayLenth 40             //times of collection
int pH_Array[arrayLenth];         //store the average value of the sensor feedback
int pH_ArrayIndex=0;

double ORP_Value;

int ORP_Array[arrayLenth];
int ORP_ArrayIndex=0;
int data_point_counter=0;

//general variables
#define voltage 5.00              //system voltage
#define printInterval 10000       //write values every 10000 milliseconds


//general formula returning average
double avergearray(int* arr, int number){
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

void setup(void)
{
        Serial.begin(9600);
        Serial.println("ORP and pH meter experiment!");

        while (!Serial) {
                ; // wait for serial port to connect. Needed for native USB port only
        }

        Serial.println("initialization done.");
}

void loop(void)
{
        static unsigned long pH_samplingTime = millis();
        static unsigned long GENERAL_printTime = millis();
        static float pH_Value, pH_voltage;

        if(millis()-pH_samplingTime > samplingInterval) //read an analog value every 20ms
        {
                pH_Array[pH_ArrayIndex++]=analogRead(pH_SensorPin);
                ORP_Array[ORP_ArrayIndex++]=analogRead(ORP_Pin);
                if(pH_ArrayIndex==arrayLenth) {
                        pH_ArrayIndex=0;
                }
                if (ORP_ArrayIndex==arrayLenth) {
                        ORP_ArrayIndex=0;
                }
                
                pH_voltage = avergearray(pH_Array, arrayLenth)*5.0/1024/6;
                pH_Value = 3.5*pH_voltage+pH_Offset;

                
                pH_samplingTime=millis()+10;
                ORP_Value=((30*(double)voltage*1000)-(75*avergearray(ORP_Array, arrayLenth)*voltage*1000/1024))/75-ORP_OFFSET;
                
        }

        if(millis() - GENERAL_printTime >= printInterval) //print to serial monitor and write to file
        {
                Serial.print(millis()/1000);
                Serial.print(" sec -- ");
                Serial.print("ORP value: ");
                Serial.print((int)ORP_Value);
                Serial.print(" mV -- ");
                Serial.print("pH value: ");
                Serial.println(pH_Value,2);

                GENERAL_printTime=millis();             
        }
}
