#! /usr/bin/python3

import displayThread
from time import sleep
from datetime import datetime


print("--- --- ---  BEE-525 - Lab 01  --- --- ---")
print("        Jose Pagan & Vincent Dang")
#count = int( input("Enter seconds to count: " ) )
#print(f"Count Down from: {count}")

## Initialize and Start the display thread
th = displayThread.displayThread()
th.start()
count = " "

while count != "exit":
    ## Get user's input
    ## count = int( input("Enter seconds to count: " ) )
    count = input("Enter seconds to count (\"exit\" to quit): " )
    if ( count == "exit" ) :
        continue
    elif ( len( count) != 1 ) | ( count < '0' ) | ( count > '9' ) :
        print(f"ERROR: Invalid input: {count} ")
        print(f"       Please enter a value btween 1 amd 9, or \"exit\" to quit")
        continue
    else:
        x=int( count )


    print(f"Count Down from: {count}")

    start_time = datetime.now()
    while x > 0:
        th.setDisplay(x)
        sleep(1)
        x -= 1

    # Capture time at end of countdoen loop
    end_time = datetime.now()

    ## Display the final zero digit
    th.setDisplay(x)

    print(f"--- Countdown comlete:")
    print(f"---         Start: { start_time.strftime('%H:%M:%S.%f')} " )
    print(f"---           End: { end_time.strftime('%H:%M:%S.%f')} " )
    print(f"--- Total Elapsed: { (end_time - start_time)} ")


## Clear the display
th.setDisplay(-1)
sleep(.4)

## Terminat the thread
print("Waiting for thread to finish")
th.stop()
th.join()

## Wait for thread complation
print(f"Conutdown Program ended.")
