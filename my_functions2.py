#   Written by LAGHEZALI MOHAMED REDA - 2018

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Pins L1, L2 Left Motor
# Pins R1, R2 Right Motor
L1 = 13
L2 = 15
R1 = 38
R2 = 40

# Ultra sonic pins
trig = 16
echo = 18

# Period for turning left/right 90 degrees (depends on the landing)
Ltime = 0.825
Rtime = 0.8

def init():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

    stop()

def cleanup():
    stop()
    time.sleep(1)
    GPIO.cleanup()

#   My motor functions

def Lforward():
	GPIO.output(L1,False)
	GPIO.output(L2,True)

def Lreverse():
	GPIO.output(L1,True)
	GPIO.output(L2,False)

def Rforward():
	GPIO.output(R1,False)
	GPIO.output(R2,True)

def Rreverse():
	GPIO.output(R1,True)
	GPIO.output(R2,False)

def stop():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    
def forward():
    Lforward()
    Rforward()
    
def reverse():
    Lreverse()
    Rreverse()

def spinLeft():
    Lreverse()
    Rforward()
    
def spinRight():
    Rreverse()
    Lforward()

def turnLeft():
    spinLeft()
    time.sleep(Ltime)
    stop()

def turnRight():
    spinRight()
    time.sleep(Rtime)
    stop()

#   My ultrasound functions

def getDistance():
    GPIO.output(trig, False)
    time.sleep(0.1)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    
    while GPIO.input(echo)==0:
        pulse_start = time.time()
    
    while GPIO.input(echo)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    return distance
