# Note: Project replaced by https://github.com/GanerCodes/ProcessManager

`python3 main.py <config>`

Name:
    Name of task
    
    Default = default
Cmd (required):
    Command to be executed  
Time:
    Time to take in seconds.
    
    Default = 10  
RunMode:  
    once: runs once on script startup
    default: runs every `time` seconds
    finished: runs every `time` seconds, only if last execution has finished
    offset: runs every `time` seconds, plus the time it the execution took
    
    Default = default

Example `config.json`:
```
[
    {
        "name": "commandName",
        "cmd": "echo hi >> hi.txt",
        "time": "0.5",
        "runMode": "default"
    }
]
```