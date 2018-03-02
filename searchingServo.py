#   Written by LAGHEZALI MOHAMED REDA - 2018

import my_functions3 as fun

def cleanup():
    print 'Cleaning up ...'
    fun.cleanup()
    print 'Done.'

fun.init()

print 'Searching Servo Program has Started ...'

try:
    fun.radarSearch(0,100)
except KeyboardInterrupt:
    cleanup()
