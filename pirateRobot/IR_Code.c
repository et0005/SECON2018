#include "stdio.h"
#include <stdlib.h>
#include "irslinger.h"        //Library to send IR message
#include <time.h>
#include <math.h>
#include <wiringPi.h>       //Library used to configure gpio pins and interrupts
#include <unistd.h>         //Library used for delay function



/* README
 
 
 Intall the following libraries (if using the Rasberry Pi):
 
 1) download the pigpio library
 
 pigpio is a library for the Raspberry which allows control of the General Purpose
 Input Outputs (GPIO).  pigpio works on all versions of the Pi.
 
 Follow the instructions in the following website to download the library:
 
 http://abyz.me.uk/rpi/pigpio/download.html
 
 2) download the ir-slinger library by following the instructions on this website:
 
 https://github.com/bschwind/ir-slinger
 
 3) download the wiringPi library by following the instructions on this website:
 
 http://wiringpi.com/download-and-install/
 
 
 The wiringPi library references the physical pins of the rasberry pi. To obtain the reference pins of the wiringpi library
 execute "gpio readall" in the command terminal
 
 To compile the code execute "gcc ir_message.c -lm -lpigpio -pthread -lrt -lwiringPi" in the command console once you are in the
 appropriate directory
 
 -----------------------------------------------------------------------------------------------------------
 
 The code begins configuring and sending the position coordinates (logical 1's for all eight bits)  via the IR LED following the NEC
 protocol. Once the start button is pressed, the message sent by the IR LED will switch to the coordinate binary code.
 The cooridinate bits will be random at the start of every match.
 
 To modify the count-down timer go to line 152
 
 For a detailed  description on how the code configures the NEC standard IR message visit:
 https://blog.bschwind.com/2016/05/29/sending-infrared-commands-from-a-raspberry-pi-without-lirc/
 
 */

/* Global variables*/

#define startButton 10  //pin 24 of the R-Pi

static volatile int startMatch = 0;

char coordinates[9]= {'0','0','0','0','0','0','0','0','\0'}; //Coordinates array
char positioning[9]= {'1','1','1','1','1','1','1','1','\0'};  //Positioning array

/* Initial Setup */


void sendIR(char coordinates[])
{
    uint32_t outPin = 11;            // The Broadcom pin number the signal will be sent on, GPIO 11/ pin 23
    int frequency = 38000;           // The frequency of the IR signal in Hz
    double dutyCycle = 0.5;          // The duty cycle of the IR signal. 0.5 means for every cycle,
    // the LED will turn on for half the cycle time, and off the other half
    int leadingPulseDuration = 9000; // The duration of the beginning pulse in microseconds
    int leadingGapDuration = 4500;   // The duration of the gap in microseconds after the leading pulse
    int onePulse = 562;              // The duration of a pulse in microseconds when sending a logical 1
    int zeroPulse = 562;             // The duration of a pulse in microseconds when sending a logical 0
    int oneGap = 1688;               // The duration of the gap in microseconds when sending a logical 1
    int zeroGap = 562;               // The duration of the gap in microseconds when sending a logical 0
    int sendTrailingPulse = 1;       // 1 = Send a trailing pulse with duration equal to "onePulse"
    // 0 = Don't send a trailing pulse
    
    
    /* Function to send IR message */
    
    int result = irSling
    (
     outPin,
     frequency,
     dutyCycle,
     leadingPulseDuration,
     leadingGapDuration,
     onePulse,
     zeroPulse,
     oneGap,
     zeroGap,
     sendTrailingPulse,
     coordinates);
    
    printf ("%s\n",coordinates);
}

/* Start button pressed*/

void interruptButton0(void)
{
    int buttonVal= digitalRead(startButton);
    if(buttonVal == 0)
    {
        startMatch=1;  //If button (pin:24) is pressed, the match will begin which will send the coordinates to the robots
    }
}

void setup()
{
    time_t t; //argument used to allow random generation of coordinates
    wiringPiSetup();
    pinMode (startButton, INPUT);
    
    wiringPiISR (startButton, INT_EDGE_BOTH, &interruptButton0);
    
    srand( (unsigned) time(NULL)); //allows use of rand()
}

/* Start a new game*/
void game()
{
    startMatch=0;
    int startedCounting = 0;
    int i=0;
    time_t finish;
    clock_t time;
    
    int bit;
    
    for (i=0;i<3;i++)  //randomizing the bits for the coordinates
    {
        bit=rand()%2; //outputs either 1's or 0's
        coordinates[i+5]= bit + 48; //manipulates and interprets the bit 5-7 interger value in the array into ASCII
    }
    
    /*Loop to send IR positiong message continuosly until button0  is pressed*/
    while(1)
    {
        sleep(0.2);  //send IR message every 200 ms
        if(startMatch==0)
        {
            sendIR(positioning); //send position code
        }
        else
        {
            sendIR(coordinates); //send coordinates code
            if(!startedCounting)
            {
                finish= (2)*CLOCKS_PER_SEC + clock();  //start the timer
                startedCounting=1;
            }
            else
            {
                time = clock();
                printf("Time left: %LF \n\n", (long double)(time-finish)/CLOCKS_PER_SEC);
                
                if(time >= finish) //if time is over, end match
                {
                    break;
                }
            }
        }
    }
    
}




//Main thread function
int main(int argc, char *argv[])
{
    setup();
    game();
    
    return 0;
}
