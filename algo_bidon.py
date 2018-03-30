#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.ultra_sonic as us
import lib.car_motors as car
import lib.servo_motor as servo
import time


def cleanup():
    print 'Stopping Obstacle Avoidance Program...'
    print 'Cleaning up Car Motors...'
    car.cleanup()
    print 'Done Cleaning up Car Motors.'
    print 'Cleaning up Ultra Sonic Sensor...'
    us.cleanup()
    print 'Done Cleaning up Ultra Sonic Sensor.'
    print 'Obstacle Avoidance Program Stoped.'
    servo.cleanup()
    print 'Done Cleaning up Servo Motor.'
    print 'Control Program Stoped.'

critical_distance = 20.0
distance = 0.0

CAR_SPEED_FORWARD = 30.5 # a z , e r t y
DELAY_360_RIGHT = 3.1 # i o p , k l m
DELAY_360_LEFT = 3.231 # q s d , f g h

bool_turn = True;
is_turning = 0 # 0 : no, 1: right, -1:left

us.init()
car.init()
servo.init()

print 'Obstacle Avoidance Program has Started ...'

#return true if obstacle exist
def find_obstacle():
    print 'Finding Obstacles...'
    dis = 0.0
    for i in range(30, 80, 10):
        servo.setServo(i)
        time.sleep(0.5)
        dis = us.getDistance()
        while dis > 500 or dis < 5:
            dis = us.getDistance()
        if dis < critical_distance:
            servo.servoMiddle()
            print 'Obstacle Found !'
            return True
    servo.servoMiddle()
    print 'No Obstacles !'
    return False

try:
    while True:
    
    
    if is_turning == 0:
            if find_obstacle() == False:
                print 'Moving Forward ...'
                car.advanceDistanceWarmUp(critical_distance/2, CAR_SPEED_FORWARD)
            else:
                if bool_turn ==  True:
                    print 'Turning Right ...'
                    car.spinModulationWarmUp(90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                    is_turning = 1
                    bool_turn = False
                else:
                    print 'Turning Left ...'
                    car.spinModulationWarmUp(-90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                    is_turning = -1
                    bool_turn = True
                print 'bool turn = ', bool_turn

        if is_turning == 1:
            servo.servoLeft()
            time.sleep(1)
            #search for hawta
            car.advanceDistanceWarmUp(25, CAR_SPEED_FORWARD)
            while us.getDistance() < critical_distance:
                servo.servoMiddle()
                time.sleep(1)
                if us.getDistance() < critical_distance: # obstacle in front while searching for hawta
                    car.spinModulationWarmUp(180, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                    is_turning = -1
                else:
                    car.advanceDistanceWarmUp(25, CAR_SPEED_FORWARD)
            if is_turning == 1:
                car.spinModulationWarmUp(-90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                is_turning = 0

        if is_turning == -1:
            servo.servoRight()
            time.sleep(1)
            #search for hawta
            car.advanceDistanceWarmUp(25, CAR_SPEED_FORWARD)
            while us.getDistance() < critical_distance:
                servo.servoMiddle()
                time.sleep(1)
                if us.getDistance() < critical_distance: # obstacle in front while searching for hawta
                    car.spinModulationWarmUp(-180, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                    is_turning = 1
                else:
                    car.advanceDistanceWarmUp(25, CAR_SPEED_FORWARD)
            if is_turning == -1:
                car.spinModulationWarmUp(90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
                is_turning = 0

except KeyboardInterrupt:
    cleanup()