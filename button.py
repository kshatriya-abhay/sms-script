import RPi.GPIO as GPIO
import time
import send_sms

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed. Sending Emergency SMS')
        sms.sendsms()
        time.sleep(0.2)
