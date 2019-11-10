#include "HX711.h"
#define calibration_factor -12000.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define DOUT  3
#define CLK  2
HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); 
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0
}
void loop() {
  Serial.print(scale.get_units(), 1); //scale.get_units() returns a float
  Serial.println();
}
