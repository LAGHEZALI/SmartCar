#   Written by LAGHEZALI MOHAMED REDA - 2018

import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Servo pins
servo = 12

def init():

    global servoMotor
    
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(servo,GPIO.OUT)

    servoMotor = GPIO.PWM(servo,50)
    servoMotor.start(7.5)
    
def cleanup():
    servoMiddle()
    stopServo()
    time.sleep(1)
    GPIO.cleanup()

#   My servo Functions

def servoMiddle():
    servoMotor.ChangeDutyCycle(7.5)

def servoLeft():
    servoMotor.ChangeDutyCycle(12.5) 

def servoRight():
    servoMotor.ChangeDutyCycle(3)

def stopServo():
    servoMotor.stop()

def setServoCycle(cycle):
    servoMotor.ChangeDutyCycle(cycle)

def setServo(radius):
    if radius<0:
        servoMotor.ChangeDutyCycle(3)
    elif radius>100:
        servoMotor.ChangeDutyCycle(12.5)
    else:
        r = radius*0.095+3
        servoMotor.ChangeDutyCycle(r)

def radarSearch(begin, end):
    if begin < 0 :
        begin = 0
    if end > 100 :
        end = 100
    
    while True:
        for x in range(begin, end):
            setServo(x)
            time.sleep(0.01)
        x=end
        while x > begin:
            setServo(x)
            time.sleep(0.01)
            x -= 1