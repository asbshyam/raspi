#!/usr/bin/python
# RasPi GPIO Controller

# Headers

import RPi.GPIO as GPIO
import time
from datetime import datetime

# Declarations

timer = 3

# Definitions


def start_motor(arg1):
    # Logic
    return


def stop_motor(arg1):
    # Logic
    return


def relay_up(arg1):
    print("Enabling Relay " + str(arg1))

    if arg1 == 1:
        # print("Relay1 ON --- GPIO18 LOW")
        GPIO.output(18, GPIO.LOW)
        # time.sleep(5)

    if arg1 == 2:
        # print("Relay2 ON --- GPIO23 LOW")
        GPIO.output(23, GPIO.LOW)
        # time.sleep(5)

    return


def relay_down(arg1):
    print("Disabling Relay - " + str(arg1))

    if arg1 == 1:
        # print("Relay1 OFF --- GPIO18 HIGH")
        GPIO.output(18, GPIO.HIGH)
        # time.sleep(2)

    if arg1 == 2:
        # print("Relay2 OFF --- GPIO23 HIGH")
        GPIO.output(23, GPIO.HIGH)
        time.sleep(2)

    return


# Main Code Begins

print("----------------------------")
print("Init...")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

time.sleep(1)

# GPIO.output(18, GPIO.LOW)
# GPIO.output(23, GPIO.LOW)
# time.sleep(1)
# GPIO.output(18, GPIO.HIGH)
# GPIO.output(23, GPIO.HIGH)

print("GPIO States : 18 & 13 -> " + str(GPIO.input(18)) + " & " + str(GPIO.input(23)))

time.sleep(1)

print("\nStart Motor for " + str(timer) + " seconds..\n")

relay_up(1)
relay_up(2)
time.sleep(timer)

print("\nStopping Motor..\n")
relay_down(1)
relay_down(2)
time.sleep(1)

print(datetime.now())
print("\nQuitting...")
print("---------------------------")

GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.cleanup()

# End Code
