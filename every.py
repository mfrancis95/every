from argparse import ArgumentParser
import subprocess
import time
from intervals import Interval

parser = ArgumentParser("every")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("delay")
parser.add_argument("-s", "--start")
parser.add_argument("-t", "--times", default = -1, type = int)
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

units = {
    "m": 60,
    "h": 3600,
    "d": 86400
}

call = lambda: (subprocess.Popen if args.async else subprocess.call)(" ".join(args.command), shell = True)
delay = args.delay.strip()
delay = float(delay[:-1]) * units.get(delay[-1], 1)
start = args.start

if start:
    now = time.localtime()
    now = now[3] * 3600 + now[4] * 60 + now[5]
    start = time.strptime(start, "%H:%M:%S")
    start = start[3] * 3600 + start[4] * 60 + start[5] - now

Interval(delay, call, start, args.times)
