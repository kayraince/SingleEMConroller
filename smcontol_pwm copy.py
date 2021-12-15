import RPi.GPIO as GPIO
from time import sleep
from RPLCD import CharLCD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=38, pin_e=40, pins_data=[37, 35, 33, 31], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8, charmap='A02', autolinebreaks=True)
lcd.write_string("initializing... ")
sleep(2)


pulse_wight = int(input("Set Wave Length"))
pulse_frequency = int(input("Set a Frequency: "))

    
confirm_ignition(pulse_frequency, pulse_wight)
    
    


def engine_set():
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    


def rotation_set():

    direction = str(input("Choose a Direction: "))
    if direction == "clockwise":
        GPIO.output(7, 1)
        GPIO.output(11, 1)
        GPIO.output(13, 0)
    else:
        GPIO.output(7, 1)
        GPIO.output(11, 0)
        GPIO.output(13, 1)
   


def confirm_ignition(pulse_frequency, pulse_wight):

    lcd.write_string("Engine Set")

    permission = str(input("Please Confirm Ignition"))
    if permission == "Confirm":
        engine_set()
        rotation_set()
        duration = float(input("Set Time Duration: "))
        pmw = GPIO.PWM(7, pulse_frequency)
        pmw.start(pulse_wight)
        sleep(duration)
        GPIO.output(7, 0)
        pmw.stop()
        lcd.clear()
        lcd.write_string("ignition complete...")
        print("ignition complete...")
        lcd.clear()
    else:
        print("ignition terminated")
        exit(1)
