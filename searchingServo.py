#   Written by LAGHEZALI MOHAMED REDA - 2018

import my_functions as fun

def cleanup():
    print 'Cleaning up ...'
    fun.cleanup()
    print 'Done.'

fun.init()

print 'Obstacle Avoidance Program has Started ...'

try:
    fun.radarSearch(37,55)
except KeyboardInterrupt:
    cleanup()
