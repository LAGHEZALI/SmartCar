#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.ultra_sonic as us
import lib.car_motors as car
import lib.servo_motor as servo
import time

#   Cleanup the components before shuting down the Smart Car

def cleanup():
    print 'Stopping Control Program...'
    print 'Cleaning up Car Motors...'
    car.cleanup()
    print 'Done Cleaning up Car Motors.'
    print 'Cleaning up Ultra Sonic Sensor...'
    us.cleanup()
    print 'Done Cleaning up Ultra Sonic Sensor.'
    print 'Cleaning up Servo Motor ...'
    servo.cleanup()
    print 'Done Cleaning up Servo Motor.'
    print 'Control Program Stoped.'

#   Some useful vatiables

critical_distance = 15.0
distance = 0.0

leftTurnSleep = 0.7
rightTurnSleep = 0.7

#   Initialize the Smart Car components

us.init()
car.init()
servo.init()

#   Our Algorithm methods

def scan():
    scanList = []
    for i in range(10, 90, 10):
        time.sleep(0.3)
        servo.setServo(i)
        time.sleep(0.3)
        scanList.append(us.getDistance())
        servo.servoMiddle()
    return scanList

#   Our Algorithm

print 'Obstacle Avoidance Program has Started ... Wish Good Luck to me'

try:
    while True:
        
        car.forward()

        distance = us.getDistance()
        
        while (distance > critical_distance):
           
            distance = us.getDistance()
        
        car.turnRight()

except KeyboardInterrupt:
    cleanup()