#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.ultra_sonic as us
import lib.car_motors as car

def cleanup():
    print 'Stopping Obstacle Avoidance Program...'
    print 'Cleaning up Car Motors...'
    car.cleanup()
    print 'Done Cleaning up Car Motors.'
    print 'Cleaning up Ultra Sonic Sensor...'
    us.cleanup()
    print 'Done Cleaning up Ultra Sonic Sensor.'
    print 'Obstacle Avoidance Program Stoped.'

critical_distance = 20.0
distance = 0.0

CAR_SPEED_FORWARD = 30.5 # a z , e r t y
DELAY_360_RIGHT = 3.1 # i o p , k l m
DELAY_360_LEFT = 3.231 # q s d , f g h

bool_turn = True;

us.init()
car.init()

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
        
        if find_obstacle() == False:
            print 'Moving Forward ...'
            car.advanceDistanceWarmUp(critical_distance/2, CAR_SPEED_FORWARD)
        else:
            if bool_turn ==  True:
                print 'Turning Right ...'
                car.spinModulationWarmUp(90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
            else:
                print 'Turning Left ...'
                car.spinModulationWarmUp(-90, 20,DELAY_360_RIGHT, DELAY_360_LEFT)
            bool_turn != bool_turn
        

except KeyboardInterrupt:
    cleanup()