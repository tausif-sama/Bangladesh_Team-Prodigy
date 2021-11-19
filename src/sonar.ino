
// This uses Serial Monitor to display Range Finder distance readings

// Include NewPing Library
#include "NewPing.h"

// Hook up HC-SR04 with Trig to Arduino Pin 9, Echo to Arduino pin 10
#define TRIGGER_PINR 3
#define ECHO_PINR 2
#define TRIGGER_PINL 6
#define ECHO_PINL 5
  

// NewPing setup of pins and maximum distance.
NewPing sonarr(TRIGGER_PINR, ECHO_PINR, 400);
NewPing sonarl(TRIGGER_PINL, ECHO_PINL, 400);
float duration;
int distancer;
int distancel;
void setup() 
{
  Serial.begin(9600);
  //Serial.setTimeout(0);
}

void loop() 
{
  // Send ping, get distance in cm
  distancer = sonarr.ping_cm();
   // Send ping, get distance in cm
  distancel = sonarl.ping_cm();
  // Send results to Serial Monitor

  Serial.print(distancer);
  Serial.print("x");
  Serial.println(distancel);

  delay(10);
}// This uses Serial Monitor to display Range Finder distance readings

// Include NewPing Library
#include "NewPing.h"

// Hook up HC-SR04 with Trig to Arduino Pin 9, Echo to Arduino pin 10
#define TRIGGER_PINR 3
#define ECHO_PINR 2
#define TRIGGER_PINL 6
#define ECHO_PINL 5
  

// NewPing setup of pins and maximum distance.
NewPing sonarr(TRIGGER_PINR, ECHO_PINR, 400);
NewPing sonarl(TRIGGER_PINL, ECHO_PINL, 400);
float duration;
int distancer;
int distancel;
void setup() 
{
  Serial.begin(9600);
  //Serial.setTimeout(0);
}

void loop() 
{
  // Send ping, get distance in cm
  distancer = sonarr.ping_cm();
   // Send ping, get distance in cm
  distancel = sonarl.ping_cm();
  // Send results to Serial Monitor

  Serial.print(distancer);
  Serial.print("x");
  Serial.println(distancel);

  delay(10);
}