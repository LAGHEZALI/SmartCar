#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.car_motors as car
import lib.servo_motor as servo
import lib.ultra_sonic as us
import sys, tty, termios, time

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

DISTANCE = 20.0
ANGLE = 90.0

CAR_SPEED_FORWARD = 31.0 # a z , e r t y
DELAY_360_RIGHT = 2.825 # i o p , k l m
DELAY_360_LEFT = 2.825 # q s d , f g h

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

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

car.init()
servo.init()
us.init()

position = 50 # servo position : between 0 and 100
step = 2 # servo step when triggered

print 'Control Porgram has Started ...'

try:
    while True:
        keyp = readkey()

        if keyp == UP:
            DISTANCE += 1
            print 'DISTANCE ++ =>', DISTANCE, 'cm'
        elif keyp == DOWN:
            DISTANCE -= 1
            print 'DISTANCE -- =>', DISTANCE, 'cm'
        elif keyp == RIGHT:
            ANGLE += 1
            print 'ANGLE ++ =>', ANGLE, 'deg'
        elif keyp == LEFT:
            ANGLE -= 1
            print 'ANGLE -- =>', ANGLE, 'deg'


        elif keyp == '8':
            car.advanceDistanceWarmUp(DISTANCE, CAR_SPEED_FORWARD)
            print 'Advance with DISTANCE=', DISTANCE
        elif keyp == '2':
            car.advanceDistanceWarmUp(-DISTANCE, CAR_SPEED_FORWARD)
            print 'Advance with -DISTANCE=', -DISTANCE
        elif keyp == '4':
            car.spinLeftModulationWarmUp(ANGLE, 20, DELAY_360_LEFT)
            print 'Turn Left with', ANGLE, 'deg'
        elif keyp == '6':
            car.spinRightModulationWarmUp(ANGLE, 2, DELAY_360_RIGHT)
            print 'Turn Right with', ANGLE, 'deg'
        elif keyp == ' ':
            car.stop()
            print 'Stop'


        elif keyp == 'a':
            CAR_SPEED_FORWARD += 0.1
            print 'CAR_SPEED_FORWARD +0.1 =>', CAR_SPEED_FORWARD, 'cm/s'
        elif keyp == 'z':
            CAR_SPEED_FORWARD += 0.01
            print 'CAR_SPEED_FORWARD +0.01 =>', CAR_SPEED_FORWARD, 'cm/s'
        elif keyp == 'e':
            CAR_SPEED_FORWARD += 0.001
            print 'CAR_SPEED_FORWARD +0.001 =>', CAR_SPEED_FORWARD, 'cm/s'
        elif keyp == 'r':
            CAR_SPEED_FORWARD -= 0.1
            print 'CAR_SPEED_FORWARD -0.1 =>', CAR_SPEED_FORWARD, 'cm/s'
        elif keyp == 't':
            CAR_SPEED_FORWARD -= 0.01
            print 'CAR_SPEED_FORWARD -0.01 =>', CAR_SPEED_FORWARD, 'cm/s'
        elif keyp == 'y':
            CAR_SPEED_FORWARD -= 0.001
            print 'CAR_SPEED_FORWARD -0.001 =>', CAR_SPEED_FORWARD, 'cm/s'
        

        elif keyp == 'q':
            DELAY_360_LEFT += 0.1
            print 'DELAY_360_LEFT +0.1 =>', DELAY_360_LEFT, 's'
        elif keyp == 's':
            DELAY_360_LEFT += 0.01
            print 'DELAY_360_LEFT +0.01 =>', DELAY_360_LEFT, 's'
        elif keyp == 'd':
            DELAY_360_LEFT += 0.001
            print 'DELAY_360_LEFT +0.001 =>', DELAY_360_LEFT, 's'
        elif keyp == 'f':
            DELAY_360_LEFT += 0.1
            print 'DELAY_360_LEFT +0.1 =>', DELAY_360_LEFT, 's'
        elif keyp == 'g':
            DELAY_360_LEFT += 0.01
            print 'DELAY_360_LEFT +0.01 =>', DELAY_360_LEFT, 's'
        elif keyp == 'h':
            DELAY_360_LEFT += 0.001
            print 'DELAY_360_LEFT +0.001 =>', DELAY_360_LEFT, 's'


        elif keyp == 'i':
            DELAY_360_RIGHT += 0.1
            print 'DELAY_360_RIGHT +0.1 =>', DELAY_360_RIGHT, 's'
        elif keyp == 'o':
            DELAY_360_RIGHT += 0.01
            print 'DELAY_360_RIGHT +0.01 =>', DELAY_360_RIGHT, 's'
        elif keyp == 'p':
            DELAY_360_RIGHT += 0.001
            print 'DELAY_360_RIGHT +0.001 =>', DELAY_360_RIGHT, 's'
        elif keyp == 'k':
            DELAY_360_RIGHT -= 0.1
            print 'DELAY_360_RIGHT -0.1 =>', DELAY_360_RIGHT, 's'
        elif keyp == 'l':
            DELAY_360_RIGHT -= 0.01
            print 'DELAY_360_RIGHT -0.01 =>', DELAY_360_RIGHT, 's'
        elif keyp == 'm':
            DELAY_360_RIGHT -= 0.001
            print 'DELAY_360_RIGHT -0.001 =>', DELAY_360_RIGHT, 's'

        
        elif keyp == '5':
            print '================================================'
            print 'DISTANCE =>', DISTANCE, 'cm'
            print 'ANGLE =>', ANGLE, 'deg'
            print 'CAR_SPEED_FORWARD =>', CAR_SPEED_FORWARD, 'cm/s'
            print 'DELAY_360_RIGHT =>', DELAY_360_RIGHT, 's'
            print 'DELAY_360_LEFT =>', DELAY_360_LEFT, 's'
            print '================================================'

        elif keyp == 'x':   
            break

    cleanup()

except KeyboardInterrupt:
    cleanup()