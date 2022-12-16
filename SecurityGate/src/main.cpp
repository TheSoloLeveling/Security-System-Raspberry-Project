#include <Arduino.h>
#include <Keypad.h>
#include <stdio.h>
#include <stdlib.h>

#define DATA_SIZE 1000

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

void setup(){
  Serial.begin(9600);
  Serial.println("Enter a 4 digit number");
}
  
void loop(){
  char Key = keypad.getKey();

  if (Key >= '0' && Key <= '9'){
    //Serial.println(Key);
      myInt = (myInt * 10) + Key -'0';
      digitCount++;
    if (digitCount == 4) {
      Serial.print("You entered: ");
      Serial.println(myInt);
      
      FILE * fPtr;
      fPtr = fopen("data/file1.txt", "w");
      if(fPtr == NULL)
        {
          printf("Unable to create file.\n");
          exit(EXIT_FAILURE);
        }
      fprintf(fPtr, "%d", myInt);
      fclose(fPtr);

      printf("File created and saved successfully. :) \n");
      
      digitCount = 0;
      myInt = 0;

    }
  }

  

}