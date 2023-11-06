import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def setOutput(ledpattern):
    GPIO.output(PIN_LATCH, 0)
    for x in range(8):
        GPIO.output(PIN_DATA, int(ledpattern[x-1]))
        GPIO.output(PIN_CLOCK, 1)
        GPIO.output(PIN_CLOCK, 0)
    GPIO.output(PIN_LATCH, 1)

try:
    for i in range(10):
        setOutput("11111111")
        time.sleep(1)
        setOutput("00000000")
        time.sleep(1)
finally:
    # Ensure LEDs are turned off
    setOutput("00000000")
    # Set pins to LOW
    GPIO.output(PIN_DATA, GPIO.LOW)
    GPIO.output(PIN_LATCH, GPIO.LOW)
    GPIO.output(PIN_CLOCK, GPIO.LOW)
    # Cleanup
    GPIO.cleanup()
