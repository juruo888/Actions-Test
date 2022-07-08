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
os.system("pwsh \"VERSION=" + "ScratchOff v" + ver + " (" + version + ") \" >> $env:GITHUB_ENV")
os.system("pwsh \"VER=" + ver + "\" >> $env:GITHUB_ENV")
with open("log.txt", "w", encoding="utf-8") as file:
    file.write(log)