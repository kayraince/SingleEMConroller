import RPi.GPIO as GPIO
from time import sleep
from RPLCD import CharLCD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=38, pin_e=40, pins_data=[37,35,33,31], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8, charmap='A02', autolinebreaks=True)
lcd.write_string("initializing... ")
sleep(2)
lcd.clear()
sleep(1)
lcd.clear()
lcd.write_string("Choose Signal Type: ")
p_type = str(input("Choose Signal Type: "))
if p_type == "PMW":
    lcd.clear()
    lcd.write_string("Signal Type Set " + str(p_type))
    lcd.write_string("Set Wave Length:")
    pulse_wight = int(input("Set Wave Length"))
    lcd.clear()
    lcd.write_string("Pulse set to "+ str(pulse_wight))
    lcd.write_string("Set a Frequency: ")
    pulse_frequency = int(input("Set a Frequency: "))
    lcd.clear()
    lcd.write_string("Frequency Set to " + str(pulse_frequency))
    lcd.write_string("Please Confirm... " + str(pulse_frequency) + str(pulse_wight))
    confirm = str(input("Please Confirm..."))
    if confirm == "confirm":
        lcd.clear()
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        lcd.write_string("Motor Online...")
        lcd.write_string("Set Time, Direction")
        duration = float(input("Set Time Duration: "))
        direction = str(input("Choose a Direction: "))
        if direction == "clockwise":
            lcd.clear()
            lcd.write_string("ignition for " + str(duration) + "sec" + str(direction))
            pmw = GPIO.PWM(7, pulse_frequency)
            pmw.start(pulse_wight)
            GPIO.output(7, 1)
            GPIO.output(11, 1)
            GPIO.output(13, 0)
            sleep(duration)
            GPIO.output(7, 0)
        else:
            lcd.clear()
            lcd.write_string("ignition for " + str(duration) + "sec" + str(direction))
            pmw = GPIO.PWM(7, pulse_frequency)
            pmw.start(pulse_wight)
            GPIO.output(7, 1)
            GPIO.output(11, 0)
            GPIO.output(13, 1)
            sleep(duration)
            GPIO.output(7, 0)
    else:
        exit()
else:
    lcd.clear()
    lcd.write_string("Signal Type Set " + str(p_type))
    lcd.write_string("Set Wave Length:")
    pulse_wight = int(input("Set Wave Length"))
    lcd.clear()
    lcd.write_string("Pulse set to " + str(pulse_wight))
    lcd.write_string("Set a Frequency: ")
    pulse_frequency = int(input("Set a Frequency: "))
    lcd.clear()
    lcd.write_string("Frequency Set to " + str(pulse_frequency))
    lcd.write_string("Please Confirm... " + str(pulse_frequency) + str(pulse_wight))
    confirm = str(input("Please Confirm..."))
    if confirm == "confirm":
        lcd.clear()
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        lcd.write_string("Motor Online...")
        lcd.write_string("Set Time, Direction")
        duration = float(input("Set Time Duration: "))
        direction = str(input("Choose a Direction: "))
        if direction == "clockwise":
            lcd.clear()
            lcd.write_string("ignition for " + str(duration) + "sec" + str(direction))
            GPIO.output(7, 1)
            GPIO.output(11, 1)
            GPIO.output(13, 0)
            sleep(duration)
            GPIO.output(7, 0)
        else:
            lcd.clear()
            lcd.write_string("ignition for " + str(duration) + "sec" + str(direction))
            GPIO.output(7, 1)
            GPIO.output(11, 0)
            GPIO.output(13, 1)
            sleep(duration)
            GPIO.output(7, 0)
    else:
        exit()
lcd.clear()
lcd.write_string("ignition complete...")
print("ignition complete...")








