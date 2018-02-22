import lib.motor as motor, curses

screen = curses.initscr()


motor.init()

try:
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)

    while True:
        char = screen.getch()
        if char == ord('x'):
            "Exiting the program ..."
            break
        elif char == curses.KEY_UP:
            print 'Forward'
            #motor.forward()
        elif char == curses.KEY_DOWN:
            print 'Reverse'
            #motor.reverse()
        elif char == curses.KEY_RIGHT:
            print 'Spin Right'
            #motor.spinLeft()
        elif char == curses.KEY_LEFT:
            print 'Spin Left'
            #motor.spinRight()
        elif char == 10:
            print 'Stop'
            #motor.stop()

finally:
    print 'Cleaning up ...'
    curses.endwin()
    #curses.nocbreak(); screen.keypad(0); curses.echo()
    motor.cleanup()
    print 'Done.'
