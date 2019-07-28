#!/usr/bin/python3
"""
Names: Kyle du Plessis
Student Number: DPLKYL002
Prac: 1
Date: 22/07/2019
"""

# import relevant libraries
import RPi.GPIO as GPIO

# set mode to BCM pin numbering system
GPIO.setmode(GPIO.BCM)

# select pins to be used from GPIO pinout diagram

# set LED1 to GPIO number 16
LED1 = 16  # corresponds to board number 36

# set LED2 to GPIO number 20
LED2 = 20  # corresponds to board number 38

# set LED3 to GPIO number 21
LED3 = 21  # corresponds to board number 40

# set btnIncrease to GPIO number 19
btnIncrease = 19  # corresponds to board number 35

# set btnDecrease to GPIO number 26
btnDecrease = 26  # corresponds to board number 37

# configure LEDs as output
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# configure push buttons as input
# both buttons are currently in up position
GPIO.setup(btnIncrease, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button to increase binary value
GPIO.setup(btnDecrease, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button to decrease binary value

# initialise global variables
# list of 3-bit binary values
binaryValues = ["000", "001", "010", "011", "100", "101", "110", "111"]
counter = 0

# this function increases the binary value on button press
def increaseBinaryValue():

    print("***Increment button pressed***")
    global counter  # use global keyword to modify counter from inside the function

    if counter == 7:  # wrap around value - increasing "111" should display "000"
        counter = 0
    else:
        counter += 1  # increment counter by 1

    # display specific binary value on 3 LEDs
    GPIO.output(LED1, int(binaryValues[counter][0]))
    GPIO.output(LED2, int(binaryValues[counter][1]))
    GPIO.output(LED3, int(binaryValues[counter][2]))

    # print out specific binary value to screen
    print("3-bit binary value: " + binaryValues[counter])


# this function decreases the binary value on button press
def decreaseBinaryValue():

    print("***Decrement button pressed***")
    global counter  # use global keyword to modify counter from inside the function

    if counter == 0:  # wrap around value - decreasing "000" should display "111"
        counter = 7
    else:
        counter -= 1  # decrement counter by 1

    # display specific binary value on 3 LEDs
    GPIO.output(LED1, int(binaryValues[counter][0]))
    GPIO.output(LED2, int(binaryValues[counter][1]))
    GPIO.output(LED3, int(binaryValues[counter][2]))

    # print out specific binary value to screen
    print("3-bit binary value: " + binaryValues[counter])

# inputs - interrupts and edge detection
# falling edge detection on btnIncrease and btnDecrease, ignoring further edges for 200ms for switch bounce handling
GPIO.add_event_detect(btnIncrease, GPIO.FALLING, callback=increaseBinaryValue, bouncetime=200) # set callback function to increaseBinaryValue function
GPIO.add_event_detect(btnDecrease, GPIO.FALLING, callback=decreaseBinaryValue, bouncetime=200) # set callback function to decreaseBinaryValue function

# program logic
def main():
    x = 1
    #print("write your logic here")


# only run the functions if
if __name__ == "__main__":
    # make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # turn off GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
