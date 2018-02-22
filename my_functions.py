import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)

# Pins L1, L2 Left Motor
# Pins R1, R2 Right Motor
L1 = 7
L2 = 11
R1 = 13
R2 = 15

# Ultra sonic pins
trig = 16
echo = 18

def init():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(R1, GPIO.OUT)
    GPIO.setup(R2, GPIO.OUT)
    
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    
    stop()

def cleanup():
    stop()
    time.sleep(1)
    GPIO.cleanup()

def Lforward():
	GPIO.output(L1,False)
	GPIO.output(L2,True)

def Lreverse():
	GPIO.output(L1,True)
	GPIO.output(L2,False)

def Rforward():
	GPIO.output(R1,False)
	GPIO.output(R2,True)

def Rreverse():
	GPIO.output(R1,True)
	GPIO.output(R2,False)


def stop():
    GPIO.output(L1,False)
    GPIO.output(L2,False)
    GPIO.output(R1,False)
    GPIO.output(R2,False)
    
def forward():
	Lforward()
	Rforward()
    
def reverse():
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

def getDistance():
    GPIO.output(trig, False)
    time.sleep(1)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    
    while GPIO.input(echo)==0:
        pulse_start = time.time()
    
    while GPIO.input(echo)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    print "->Distance:",distance,"cm"    