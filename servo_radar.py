#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.servo_motor as servo, time

def cleanup():
    print 'Cleaning up Servo Motor ...'
    servo.cleanup()
    print 'Done Cleaning up Servo Motor.'

servo.init()

begin = 0
end = 100

print 'Servo Radar Program has Started ...'

try:
    if begin < 0 :
        begin = 0
    if end > 100 :
        end = 100
    
    while True:
        for x in range(begin, end):
            servo.setServo(x)
            time.sleep(0.005)
        x=end
        while x > begin:
            servo.setServo(x)
            time.sleep(0.005)
            x -= 1
except KeyboardInterrupt:
    cleanup()
