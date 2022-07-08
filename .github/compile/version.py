import json
import os
import linecache
major = int(linecache.getline("ScratchOff.py", 31)[8:])
minor = int(linecache.getline("ScratchOff.py", 32)[8:])
releases = int(linecache.getline("ScratchOff.py", 33)[11:])
build = int(linecache.getline("ScratchOff.py", 34)[8:])
typenum = int(linecache.getline("ScratchOff.py", 35)[10:])
x = int(linecache.getline("ScratchOff.py", 36)[4:])
version = str(major) + "." + str(minor) + "." + str(releases) + \
    "." + str(build) + "." + str(typenum) + "." + str(x)
rb = json.loads(os.environ["MSG"])[-1].split("\n\n")
ver = rb[0][4:]
log = rb[1]
os.system("powershell \"VERSION=" + "ScratchOff v" + ver + " (" + version + ") \" | Out-File -FilePath >> $env:GITHUB_ENV -Encoding utf8 -Append")
os.system("powershell \"VER=" + ver + "\" | Out-File -FilePath >> $env:GITHUB_ENV -Encoding utf8 -Append")
with open("log.txt", "w") as file:
    file.write(log)