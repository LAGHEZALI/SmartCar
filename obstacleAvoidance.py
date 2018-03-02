#   Written by LAGHEZALI MOHAMED REDA - 2018

import my_functions2 as fun

def cleanup():
    print 'Cleaning up ...'
    fun.cleanup()
    print 'Done.'

distance = 0.0

fun.init()

print 'Obstacle Avoidance Program has Started ...'

try:
    while True:
        
        fun.forward()
        
        distance = fun.getDistance()

        while (distance > 40):
            print 'Distance =', distance, 'cm ---> Forward'
            distance = fun.getDistance()
            
        fun.turnRight()
        print ''
        print '!!! Distance =', distance, 'cm ---> Turning Right'
        print ''
except KeyboardInterrupt:
    cleanup()