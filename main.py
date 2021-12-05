from subprocess import Popen, DEVNULL as NULL
from json import load as loadJson
from threading import Thread
from time import sleep
from sys import argv

def run(cmd):
    return Popen(cmd, stdout = NULL, stderr = NULL, shell = True)

def runner(name, cmd, time, runMode, processes):
    if runMode == "once":
        processes.append(p := run(cmd))
        p.wait()
        processes.remove(p)
        return
    
    if runMode == "default":
        while True:
            processes.append(p := run(cmd))
            sleep(time)
    
    if runMode == "finished":
        p = None
        while True:
            finished = False
            if p is None or (finished := (p.poll() is not None)): # start or has finished
                if finished: processes.remove(p) # Remove from process list if it's finished
                processes.append(p := run(cmd))
            
            sleep(time)
    
    if runMode == "offset":
        while True:
            processes.append(p := run(cmd))
            p.wait()
            processes.remove(p)
            sleep(time)

config = loadJson(open(argv[1] if len(argv) > 1 else "config.json", "r"))

processes = []
for t in [((runnerThread := Thread(target = runner, args = (
    e["name"] if "name" in e else "default",
    e["cmd"],
    float(e["time"]) if "time" in e else 10,
    e["runMode"] if "runMode" in e else "default", processes
))), runnerThread.start()) for e in config]: t[0].join()