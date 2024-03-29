import time
import RPi.GPIO as GPIO

pin = 18
wait = 1


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)


def lit():
    setup()
    GPIO.output(pin, True)
    time.sleep(wait)
    GPIO.output(pin, False)

    GPIO.cleanup()


def blink():
    setup()
    for i in range(10):
        GPIO.output(pin, True)
        time.sleep(wait)
        GPIO.output(pin, False)
        time.sleep(wait)

    GPIO.cleanup()
