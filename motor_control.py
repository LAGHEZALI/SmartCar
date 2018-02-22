import lib.motor as motor, curses

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

motor.init()

try:
    while True:   
        char = screen.getch()
        if char == ord('x'):
            break
        elif char == curses.KEY_UP:
        	motor.forward()
        elif char == curses.KEY_DOWN:
        	motor.reverse()
        elif char == curses.KEY_RIGHT:
        	motor.spinLeft()
        elif char == curses.KEY_LEFT:
        	motor.spinRight()
        elif char == 10:
        	motor.stop()

except KeyboardInterrupt:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    motor.cleanup()
             
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    motor.cleanup()