from argparse import ArgumentParser
import subprocess
import time

parser = ArgumentParser("every")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("interval")
parser.add_argument("-s", "--start")
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

units = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400
}

call = subprocess.Popen if args.async else subprocess.call
interval = args.interval
interval = float(interval[:-1]) * units[interval[-1]]
start = args.start
command = " ".join(args.command)

if start:
    now = time.localtime()
    now = now[3] * 3600 + now[4] * 60 + now[5]
    start = time.strptime(start, "%H:%M:%S")
    start = start[3] * 3600 + start[4] * 60 + start[5] - now
    if start > 0:
        time.sleep(start)

while True:
    time.sleep(interval)
    call(command, shell = True)
