#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.ultra_sonic as us
import lib.car_motors as car
import lib.servo_motor as servo
import time
import math
import random

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

distance = 0.0

left_turn_sleep = 0.7
right_turn_sleep = 0.7

safety_distance = 20
max_angle = 180
scan_list = []
scan_list_size = 11
d_point = [50, 50]
f_point = [50, 10000050]
direction_goal = 0

#   Initialize the Smart Car components

us.init()
car.init()
servo.init()

#   Our Algorithm methods


def scan():
    scanList = []
    for i in range(10, 100, 10):
        time.sleep(0.3)
        servo.setServo(i)
        time.sleep(0.3)
        scanList.append(us.getDistance())
    servo.servoMiddle()
    return scanList


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2+(p1[1]-p2[1])**2)


def get_r_angle(scanList):
    m = scan_list_size/2
    up = 0
    down = 0
    a0 = max_angle/scan_list_size * scan_list_size/2
    for value in scanList:
        up += a0 * value
        a0 = a0 - max_angle/scan_list_size
        down = down + value
    ans = up/down
    return ans


def get_angle(p0, p1):
    [x1, y1] = p0
    [x2, y2] = p1
    a = math.degrees(math.atan((y1 - y2)/(x1 - x2+0.001)))
    if x2 >= x1:
        b = 90 + a
    else:
        b = 270 + a
    return b


def angle_to_sleep_time(angle):
    return angle*0.7/90

#   Our Algorithm

print 'Obstacle Avoidance Program has Started ... Wish Me Good Luck !'

try:
    while True:
        print 'start scan'
        scan_list = scan()
        print 'end scan'
        i = 0
        obstacle = []
        for value in scan_list:
            if value < safety_distance:
                obstacle.append(0)
            i += 1
        ang_t = get_r_angle(scan_list)
        directionToFin = get_angle(d_point, f_point)
        if len(obstacle) == 0:
            print 'Nothing here !'
        else:
            car.spinModulation(angle_to_sleep_time(ang_t), 20)
            direction_goal = ang_t
        if ang_t > 0:
            car.advance(scan_list[5 - ang_t % 5] / 2)
        else:
            car.advance(scan_list[5 + (-ang_t) % 5] / 2)


except KeyboardInterrupt:
    cleanup()
