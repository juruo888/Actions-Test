import json
import os
rb = json.loads(os.environ["MSG"])[-1].split("\n\n")
version = rb[0][4:]
log = rb[1]
os.system("setx VERSION %s" % "ScratchOff v" + version + " (" + os.environ["VERSION"] + ") ")
with open("log.txt", "w") as file:
    file.write(log)