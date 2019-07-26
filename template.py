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



# program logic
def main():
    print("write your logic here")


# only run the functions if
if __name__ == "__main__":
    # make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
