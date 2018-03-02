#   Written by LAGHEZALI MOHAMED REDA - 2018

import my_functions as fun, sys, tty, termios

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
    print 'Cleaning up ...'
    fun.cleanup()
    print 'Done.'

fun.init()

position = 50 # between 0 and 100
step = 2

print 'The Program has Started ...'

try:
    while True:
        keyp = readkey()

        #   Motors
        
        if keyp == 'w' or keyp == UP:
            fun.forward()
            print 'Forward'
        elif keyp == 's' or keyp == DOWN:
            fun.reverse()
            print 'Reverse'
        elif keyp == 'd' or keyp == RIGHT:
            fun.spinRight()
            print 'Spin Right'
        elif keyp == 'a' or keyp == LEFT:
            fun.spinLeft()
            print 'Spin Left'
        elif keyp == '4':
            fun.turnLeft()
            print 'Turn Left 90 degree'
        elif keyp == '6':
            fun.turnRight()
            print 'Turn Right 90 degree'
        elif keyp == '7':
            fun.Lforward()
            print 'Lforward'
        elif keyp == '9':
            fun.Rforward()
            print 'Rforward'
        elif keyp == '1':
            fun.Lreverse()
            print 'Lreverse'
        elif keyp == '3':
            fun.Rreverse()
            print 'Rreverse'
        elif keyp == ' ':
            fun.stop()
            print 'Stop'

        #   UltraSound Sensor
        
        elif keyp == 't':
            print 'distance =', fun.getDistance(), "cm" 

        #   Servo Motor

        elif keyp == 'i':
            position = 50
            fun.setServo(position)
            print 'Servo set to Middle Position'
        elif keyp == 'o':
            position = 0
            fun.setServo(position)
            print 'Servo set to Left Position'
        elif keyp == 'p':
            position = 100
            fun.setServo(position)
            print 'Servo set to Right Position'
        
        elif keyp == 'y':
            if position < 100:
                position += step
                fun.setServo(position)
                print 'Servo Position +', step, '=', position
        elif keyp == 'u':
            if position > 0:
                position -= step
                fun.setServo(position)
                print 'Servo Position -', step, '=', position
        
        #   Quit the Program

        elif keyp == 'x':
            break

    print 'Exiting Program ...'
    cleanup()

except KeyboardInterrupt:
    cleanup()