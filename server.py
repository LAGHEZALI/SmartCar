import lib.servo_motor as servo
import sys
import tty
import termios
from socket import *

fun.init()

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
                        servo.setServo(int(data))
                        print 'Servo Position', '=', int(data)
        except KeyboardInterrupt:
                fun.stopServo()
                fun.cleanup()
tcpSerSock.close();