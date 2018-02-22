import RPi.GPIO as GPIO, time

#GPIO.setwarnings(False)

# Pins L1, L2 Left Motor
# Pins R1, R2 Right Motor
L1 = 7
L2 = 11
R1 = 13
R2 = 15

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    stop()

def cleanup():
    stop()
    time.sleep(1)
    GPIO.cleanup()

def stop():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    
def forward():
    GPIO.output(L1,True)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    print '-----> forward'
    
def reverse():
    GPIO.output(L1,False)
    GPIO.output(L2,True)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    print '-----> reverse'

def spinLeft():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    
def spinRight():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)