from argparse import ArgumentParser
import subprocess
from time import sleep

parser = ArgumentParser("every")
parser.add_argument("-a", action = "store_true")
parser.add_argument("interval")
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

call = subprocess.Popen if args.a else subprocess.call
interval = args.interval
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
process = " ".join(args.command)

while True:
    sleep(interval)
    call(process, shell = True)
