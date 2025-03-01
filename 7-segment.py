
######################################################################
## Please use the following code to configure the 7-segment display ##
## Created by Madhava Vemuri 										##
## Date 2/25/25														##
## Please use the following circuit diagram in page 24 to make the 	##
## connections. Double check the connections before you turn the Pi ##
######################################################################

import RPi.GPIO as GPIO 	#Import the Raspberry Pi GPIO Library

# Data for segment values, without the decimal point
displayPattern = {
   #### a b c d e f g
   ' ':(0,0,0,0,0,0,0),
     0:(1,1,1,1,1,1,0),
     1:(0,1,1,0,0,0,0),
     2:(1,1,0,1,1,0,1),
     3:(1,1,1,1,0,0,1),
     4:(0,1,1,0,0,1,1),
     5:(1,0,1,1,0,1,1),
     6:(1,0,1,1,1,1,1),
     7:(1,1,1,0,0,0,0),
     8:(1,1,1,1,1,1,1),
     9:(1,1,1,1,0,1,1)
}
 
# 7 Segment Display has 7 pins connected to the cathode of the LEDs 
# Here is the breakdown of the pins used to connect the LED
LED_pin_a  = 17 # Even though the it is pin 11, based on the GPIO pin digram it is pin 17
LED_pin_b  = 18 # LED cathode to b  is connected to GPIO 18 which is pin 12
LED_pin_c  = 27 # LED cathode to c  is connected to GPIO 27 which is pin 13
LED_pin_d  = 22 # LED cathode to d  is connected to GPIO 22 which is pin 15
LED_pin_e  = 23 # LED cathode to e  is connected to GPIO 23 which is pin 18
LED_pin_f  = 24 # LED cathode to f  is connected to GPIO 24 which is pin 18
LED_pin_g  = 25 # LED cathode to g  is connected to GPIO 25 which is pin 22
LED_pin_DP = 26 # LED cathode to DP is connected to GPIO 26 which is pin 37

## Array of pins for indexing
ledPins = [ LED_pin_a, LED_pin_b, LED_pin_c, LED_pin_d, LED_pin_e, LED_pin_f, LED_pin_g, LED_pin_DP ]

# Constants for decimal point 
DP_OFF     = 0  # Decimal point OFF
DP_On      = 1  # Decimal point ON



class sevenSegment():
    ## Initialization of Display
    def __init__(self):
        self.val        = -1
        self.DP         = DP_OFF
        self.segPattern = displayPattern[' ']
        # Set the PIN mode to either BCM mode or BOARD mode 
        GPIO.setmode(GPIO.BCM) #Here we are setting the BCM mode

        # Setup the pin as output
        for i in range( len(ledPins) ):
            GPIO.setup(ledPins[i], GPIO.OUT) # Here this sets the GPIO PIN as OUTPUT

    def setValue(self, newVal, dpVal=DP_OFF):
        if ( newVal < 0 ) | (newVal > 9):
            # Error, out of range
            self.val        = -1
            self.segPattern = displayPattern[' ']
            self.DP         = DP_ON
        else:
            # Value is in range
            self.val        = newVal
            self.segPattern = displayPattern[newVal]
            self.DP         = dpVal

    def writeDisplay(self, dpVal=DP_OFF):
        self.DP = dpVal
        print(f" Dilpay value: {self.val} -- Pattern: {self.segPattern}, DP: {self.DP}")
        for j in range( len(self.segPattern) ):
            print(f"    LED_pin_{ chr( ord('a') + j ) }: {self.segPattern[j]}")
        print(f"   LED_pin_DP: {self.DP}")


## Unit Test Code:
if __name__ == '__main__':
    print(displayPattern[' '])
    for i in range(10):
      print(f"{i}: {displayPattern[i]}")

    myDigit = sevenSegment()

    for i in range(10):
        myDigit.setValue(i)
        myDigit.writeDisplay()
        
    print(ledPins)



# Turning on the LED by passing output LOW to the LED
# for example to create digit 3 the logic is given below
#(a=LOW,b=LOW,c=LOW,d=LOW,e=HIGH,f=HIGH,g=LOW,DP=LOW) 
GPIO.output(LED_pin_a,GPIO.LOW)
GPIO.output(LED_pin_b,GPIO.LOW) 
GPIO.output(LED_pin_c,GPIO.LOW)
GPIO.output(LED_pin_d,GPIO.LOW) 
GPIO.output(LED_pin_e,GPIO.HIGH)
GPIO.output(LED_pin_f,GPIO.HIGH) 
GPIO.output(LED_pin_g,GPIO.LOW)
GPIO.output(LED_pin_DP,GPIO.LOW) 