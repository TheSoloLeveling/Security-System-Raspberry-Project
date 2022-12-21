#include <Arduino.h>
#include <Keypad.h>
#include <stdio.h>
#include <stdlib.h>

#define DATA_SIZE 1000

#include<SoftwareSerial.h>

#define TxD 1
#define RxD 0

const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns

char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; //connect to the column pinouts of the keypad
int myInt = 0;
byte digitCount = 0;
//Create an object of keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
SoftwareSerial bluetoothSerial(TxD, RxD);
char c;
void setup(){
  bluetoothSerial.begin(9600);
  Serial.begin(9600);
}
  
void loop(){
  char Key = keypad.getKey();
  
  if (Key >= '0' && Key <= '9'){
    //Serial.println(Key);
      myInt = (myInt * 10) + Key -'0';
      digitCount++;
    if (digitCount == 4) {
        Serial.println(myInt);
        if(bluetoothSerial.available()){
          c = bluetoothSerial.read();
        }
      digitCount = 0;
      myInt = 0;
      

    }
  }




}