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

import sevenSegment as seg
from sevenSegment import DP_ON
from sevenSegment import DP_OFF


# custom thread class as 7 segment driver
class displayThread(Thread):

    # Initialize the thread 
    def __init__(self):
        ## need to initiaze the parent class
        Thread.__init__(self)
        ## Set default attributes
        self.display   = -1
        self.runThread =  1
        # Create an instance for a signle 7 segment display
        self.digit = seg.sevenSegment()
        self.digit.setDisplay(-1, 1)
        self.digit.showDisplay(1)

    # override the run function
    def run(self):
        # Thread's loop, run while attribute "runThread" is 1 
        while self.runThread == 1:
          # algoritm is to refresh display every .3 seconde
          self.digit.showDisplay()
          sleep(.1)

    # call segmentDisplay.setDisplay to store the new value 
    def setDisplay(self, val, dp=0):
        self.display = val
        self.DB=dp
        self.digit.setDisplay(val, dp)


    def stop(self):
        self.runThread = 0


## Unit Test Code:
if __name__ == '__main__':
    print(displayPattern[' '])
