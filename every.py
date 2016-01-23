from argparse import ArgumentParser
import subprocess
from time import sleep

parser = ArgumentParser("every")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("interval")
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
command = " ".join(args.command)

while True:
    sleep(interval)
    call(command, shell = True)
