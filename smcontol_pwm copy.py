import RPi.GPIO as GPIO
from time import sleep
from RPLCD import CharLCD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=38, pin_e=40, pins_data=[37, 35, 33, 31], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8, charmap='A02', autolinebreaks=True)
lcd.write_string("initializing... ")
sleep(2)
lcd.clear()
pulse_lambda = int(input("Pulse Wight: "))
pulse_frequency = int(input("Pulse Frequency: "))
pulse_duration = int(input("Pulse Duration: "))
pulse_direction = str(input("Pulse Direction: "))
confirm_ignition = str(input("confirm ignition: "))

def safeGuard(decision):
    if decision == "confirm":
        ignition(pulse_frequency, pulse_lambda, pulse_direction, pulse_duration)
    else:

        print("terminated")
        exit(1)



def ignition(pulse_frequenc, pulse_lambd, pulse_directio, pulse_duratio):
    engine_set()
    rotation_set(pulse_directio)
    pmw = GPIO.PWM(7, pulse_frequenc)
    pmw.start(pulse_lambd)
    sleep(pulse_duratio)
    pmw.stop()
    kill()




def engine_set():
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)


def rotation_set(direction):

    if direction == "clockwise":
        GPIO.output(7, 1)
        GPIO.output(11, 0)
        GPIO.output(13, 1)
    else:
        GPIO.output(7, 1)
        GPIO.output(11, 1)
        GPIO.output(13, 0)


def kill():
    GPIO.output(7, 0)


safeGuard(confirm_ignition)
