#   Written by LAGHEZALI MOHAMED REDA - 2018

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Pins L1, L2 Left Motor
# Pins R1, R2 Right Motor
L1 = 13
L2 = 15
R1 = 38
R2 = 40

# Period for turning left/right 90 degrees (depends on the landing)
Ltime = 0.825
Rtime = 0.8

# Period for advancing with exacltly the same size as the smartCar (depends on the landing)
car_lenght = 25.25
car_speed = 31.0

delay360 = 2.825 # delay to spin 360 degree


def init():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    
    stop()

def cleanup():
    stop()
    time.sleep(1)
    GPIO.cleanup()

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

def spinLeftFor(delay):
    Lreverse()
    Rforward()
    time.sleep(delay)
    stop()
    
def spinRightFor(delay):
    Rreverse()
    Lforward()
    time.sleep(delay)
    stop()

def spinModulation(angle, steps):
    print '==== ANGLE ====', angle
    if angle == 0:
        return
    print '==== DELAY ====', angleToDelay(angle)
    if angle < 0:
        angle = -angle
        for i in range(1,steps+1):
            spinLeftFor(angleToDelay(angle)/steps)
    else:
        for i in range(1,steps+1):
            spinRightFor(angleToDelay(angle)/steps)

def turnRight():
    spinRight()
    time.sleep(Rtime)
    stop()


def advanceDistance(distance):
    if distance < 0:
        reverse()
        distance = -distance
    else:
        forward()
    time.sleep(distance/car_speed)
    stop()

def nanoSpin(step):
    if step > 0:
        spinRight()
        time.sleep(step)
        stop()
    else:
        spinLeft()
        time.sleep(step)
        stop()


def angleToDelay(angle):
    return float(angle) * float(delay360) / 360


def angleToDelayWarmUp(angle, delay):
    return float( (int(angle)%361) ) * float(delay) / 360
    

def spinRightModulationWarmUp(angle, steps, delay):
    if angle == 0:
        return
    if angle < 0:
        angle = -angle
    for i in range(1,steps+1):
        spinRight()
        time.sleep(angleToDelayWarmUp(angle, delay)/steps)
        stop()

def spinLeftModulationWarmUp(angle, steps, delay):
    if angle == 0:
        return
    if angle < 0:
        angle = -angle
    for i in range(1,steps+1):
        spinLeft()
        time.sleep(angleToDelayWarmUp(angle, delay)/steps)
        stop()


def advanceDistanceWarmUp(distance, cs):
    if distance < 0:
        reverse()
        distance = -distance
    else:
        forward()
    time.sleep(distance/cs)
    stop()