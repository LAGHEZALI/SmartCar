#   Written by LAGHEZALI MOHAMED REDA - 2018

import my_functions as fun

def cleanup():
    print 'Cleaning up ...'
    fun.cleanup()
    print 'Done.'

fun.init()

print 'Searching Servo Program has Started ...'

try:
    fun.radarSearch(30,70)
except KeyboardInterrupt:
    cleanup()
