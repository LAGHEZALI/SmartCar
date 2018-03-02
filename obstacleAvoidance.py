#   Written by LAGHEZALI MOHAMED REDA - 2018

import lib.ultra_sonic as us
import lib.car_motors as car

def cleanup():
    print 'Stopping Obstacle Avoidance Program...'
    print 'Cleaning up Car Motors...'
    car.cleanup()
    print 'Done Cleaning up Car Motors.'
    print 'Cleaning up Ultra Sonic Sensor...'
    us.cleanup()
    print 'Done Cleaning up Ultra Sonic Sensor.'
    print 'Obstacle Avoidance Program Stoped.'

critical_distance = 20.0
distance = 0.0

us.init()
car.init()

print 'Obstacle Avoidance Program has Started ...'

try:
    while True:
        
        car.forward()

        distance = us.getDistance()
        
        while (distance > critical_distance):
           
            distance = us.getDistance()
        
        car.turnRight()

except KeyboardInterrupt:
    cleanup()