import json
import os
rb = json.loads(os.environ["MSG"])[-1].split("\n\n")
version = rb[0][4:]
log = rb[1]
os.system("powershell \"VERSION=" + "ScratchOff v" + version + " (" + os.environ["VERSION"] + ") \" | Out-File -FilePath >> $env:GITHUB_ENV -Encoding utf8 -Append")
with open("log.txt", "w") as file:
    file.write(log)