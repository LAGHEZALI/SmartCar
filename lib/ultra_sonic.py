#   Written by LAGHEZALI MOHAMED REDA - 2018

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Ultra sonic pins
trig = 16
echo = 18

def init():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

def cleanup():
    time.sleep(1)
    GPIO.cleanup()

def getDistance():
    GPIO.output(trig, False)
    time.sleep(0.1)

    GPIO.output(trig, True)
    time.sleep(0.001)
    GPIO.output(trig, False)
    
    while GPIO.input(echo)==0:
        pulse_start = time.time()
    
    while GPIO.input(echo)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    return distance