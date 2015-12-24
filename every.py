import sys
from subprocess import call
from time import sleep

arg_length = len(sys.argv)

if arg_length >= 3:
    interval = sys.argv[1]
    unit = "s"
    index = 0
    for c in interval:
        index += 1
        if not c.isdigit():
            unit = c
            break
    interval = int(interval[0:index - 1])
    if unit == "m":
        interval *= 60
    elif unit == "d":
        interval *= 86400
    process = sys.argv[2]
    for i in range(3, arg_length):
        process += " " + sys.argv[i]
    while True:
        sleep(interval)
        call(process, shell = True)        
