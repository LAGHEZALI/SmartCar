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

print 'The Program has Started ...'

try:
    while True:
        keyp = readkey()
        if keyp == 'w' or keyp == UP:
            fun.Lforward()
            #print 'Forward'
        elif keyp == 's' or keyp == DOWN:
            fun.Lreverse()
            #print 'Reverse'
        elif keyp == 'd' or keyp == RIGHT:
            fun.Rreverse()
            #print 'Spin Right'
        elif keyp == 'a' or keyp == LEFT:
            fun.Rforward()
            #print 'Spin Left'
        elif keyp == 'u' or keyp == LEFT:
            print "Distance:",fun.getDistance(),"cm"   
        elif keyp == ' ':
            fun.stop()
            print 'Stop'
        elif keyp == 'x':
            break

    print 'Exiting Program ...'
    cleanup()

except KeyboardInterrupt:
    cleanup()