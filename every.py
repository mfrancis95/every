from argparse import ArgumentParser
import subprocess
import time
from intervals import Interval

parser = ArgumentParser("every")
parser.add_argument("delay")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("-n", "--now", action = "store_true")
parser.add_argument("-s", "--start")
parser.add_argument("-t", "--times", default = -1, type = int)
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

units = {"m": 60, "h": 3600, "d": 86400}

call = subprocess.Popen if args.async else subprocess.call
command = " ".join(args.command)
func = lambda: call(command, shell = True)
delay = args.delay.strip()
delay = float(delay[:-1]) * units.get(delay[-1], 1)
start = args.start

if start:
    if args.now:
        func()
    start = start.strip()
    try:
        start = time.strptime(start, "%H:%M:%S")
        now = time.localtime()
        now = now[3] * 3600 + now[4] * 60 + now[5]
        start = start[3] * 3600 + start[4] * 60 + start[5] - now
    except ValueError:
        start = float(start[:-1]) * units.get(start[-1], 1)

Interval(delay, func, start, args.times)
