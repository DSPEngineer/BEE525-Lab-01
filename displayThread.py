#! /usr/bin/python3
######################################################################
# This file extends the threading class and creates a theread to     #
# drive a 7 segment LED display, connected to a RaspberryPi 4b.      #
#                                                                    #
#  Created by Jose Pagan & Vincent Dang						         #
#  Date 2/26/25														 #
######################################################################

from threading import Thread
from time import sleep
from datetime import datetime

import sevenSegment


# custom thread class as 7 segment driver
class displayThread(Thread):
    # Initialize the thread 
    def __init__(self):
        ## need to initiaze the parent class
        Thread.__init__(self)
        # Create an instance for a signle 7 segment display
        digit = sevenSegment()
        
        digit.setDisplay()
        myDigit.showDisplay()
        

        self.display   = -1
        self.runThread =  1
        print(f"Initializing thread to run={self.runThread}.")
        print(f"  Display: {self.display}")

    # override the run function
    def run(self):

        while self.runThread == 1:
          sleep(.3)
          # display a message
          print(f", {self.display}", end='')

    def setDisplay(self, val):
        self.display = val
        print(f"\n  -- New: {self.display}", end='')

    def stop(self):
        self.runThread = 0
