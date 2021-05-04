#!/usr/bin/python3
import subprocess
import json
print("Conten-type: text/html")
print()

# for obtaining in list format
img='docker images --format \"{{.Repository}}\"'
tag='docker images --format \"{{.Tag}}\"'
ID='docker images --format \"{{.ID}}\"'
imgls=(subprocess.getoutput('sudo '+img)).split("\n")
tagls=(subprocess.getoutput('sudo '+tag)).split("\n")
idls=(subprocess.getoutput('sudo '+ID)).split("\n")
db={"images":imgls,"versions":tagls,"ids":idls}
js=json.dumps(db)
print(js)
