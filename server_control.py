import lib.car_motors as car
import lib.servo_motor as servo
import lib.ultra_sonic as us
import sys
import tty
import termios
from socket import *

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

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'Waiting for connection'
    tcpCliSock,addr = tcpSerSock.accept()
    print '...connected from :', addr
    try:
        while True:
            data = ''
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                    break
            
            if data == 'forward':
                    car.forward()
                print 'Forward'
            elif data == 'reverse':
                car.reverse()
                print 'Reverse'
            elif data == 'spinRight':
                car.spinRight()
                print 'Spin Right'
            elif data == 'spinLeft':
                car.spinLeft()
                print 'Spin Left'
            elif data == 'turnLeft':
                car.turnLeft()
                print 'Turn Left 90 degree'
            elif data == 'turnRight':
                car.turnRight()
                print 'Turn Right 90 degree'
            elif data == '7':
                car.Lforward()
                print 'Lforward'
            elif data == '9':
                car.Rforward()
                print 'Rforward'
            elif data == '1':
                car.Lreverse()
                print 'Lreverse'
            elif data == '3':
                car.Rreverse()
                print 'Rreverse'
            elif data == 'stop':
                car.stop()
                print 'Stop'

            #   UltraSound Sensor
            
            elif data == 'distance':
                print 'distance =', us.getDistance(), "cm" 

            #   Servo Motor

            elif data == 'servoMid':
                position = 50
                servo.setServo(position)
                print 'Servo set to Middle Position'
            elif data == 'o':
                position = 0
                servo.setServo(position)
                print 'Servo set to Left Position'
            elif data == 'p':
                position = 100
                servo.setServo(position)
                print 'Servo set to Right Position'
            
            elif data == 'servoRight':
                if position < 100:
                    position += step
                    servo.setServo(position)
                    print 'Servo Position +', step, '=', position
            elif data == 'servoLeft':
                if position > 0:
                    position -= step
                    servo.setServo(position)
                    print 'Servo Position -', step, '=', position
            
            #   Quit the Program

            elif data == 'quit':
                break

    except KeyboardInterrupt:
            cleanup()
tcpSerSock.close();