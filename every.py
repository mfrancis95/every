import sys
from time import sleep
from subprocess import call

if len(sys.argv) >= 3:
    interval = sys.argv[1]
    for i in range(len(interval)):
        unit = interval[i]
        if unit.isalpha():
            if unit == "m":
                unit = 60
            elif unit == "h":
                unit = 3600
            elif unit == "d":
                unit = 86400
            else:
                unit = 1
            interval = float(interval[:i]) * unit
            break
    if type(interval) is str:
        interval = float(interval)
    process = " ".join(sys.argv[2:])
    while True:
        sleep(interval)
        call(process, shell = True)
