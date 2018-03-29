#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.car_motors as car
import lib.servo_motor as servo
import lib.ultra_sonic as us
import sys, tty, termios, time

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

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

        #   Motors
        
        if keyp == 'w' or keyp == UP:
            car.forward()
            print 'Forward'
        elif keyp == 's' or keyp == DOWN:
            car.reverse()
            print 'Reverse'
        elif keyp == 'd' or keyp == RIGHT:
            car.spinRight()
            print 'Spin Right'
        elif keyp == 'a' or keyp == LEFT:
            car.spinLeft()
            print 'Spin Left'
        elif keyp == '8':
            car.advance(1)
            print 'Advance 1 Step'
        elif keyp == '2':
            car.advance(-1)
            print 'Advance -1 Step'
        elif keyp == '4':
            car.spinModulation(-0.8, 20)
            #car.spinLeftFor(0.7)
            print 'Turn Left 90 degree (Modulation)'
        elif keyp == '6':
            car.spinModulation(0.8, 20)
            #car.spinRightFor(0.7)
            print 'Turn Right 90 degree (Modulation)'
        elif keyp == '7':
            car.Lforward()
            print 'Lforward'
        elif keyp == '9':
            car.Rforward()
            print 'Rforward'
        elif keyp == '1':
            car.Lreverse()
            print 'Lreverse'
        elif keyp == '3':
            car.Rreverse()
            print 'Rreverse'
        elif keyp == ' ':
            car.stop()
            print 'Stop'

        #   UltraSound Sensor
        
        elif keyp == 't':
            print 'distance =', us.getDistance(), "cm" 

        #   Servo Motor

        elif keyp == 'i':
            position = 50
            servo.setServo(position)
            print 'Servo set to Middle Position'
        elif keyp == 'o':
            position = 0
            servo.setServo(position)
            print 'Servo set to Left Position'
        elif keyp == 'p':
            position = 100
            servo.setServo(position)
            print 'Servo set to Right Position'
        
        elif keyp == 'y':
            if position < 100:
                position += step
                servo.setServo(position)
                print 'Servo Position +', step, '=', position
        elif keyp == 'u':
            if position > 0:
                position -= step
                servo.setServo(position)
                print 'Servo Position -', step, '=', position
        
        #   Quit the Program

        elif keyp == 'x':   
            break

        elif keyp == '5':
            scanList = []
            for i in range(10, 90, 5):
                servo.setServo(i)
                time.sleep(0.6)
                scanList.append(us.getDistance())
            print '  ===  '.join(map(str, scanList))
            servo.servoMiddle()


    cleanup()

except KeyboardInterrupt:
    cleanup()