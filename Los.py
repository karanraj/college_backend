#!/usr/bin/python3
import subprocess
import json
print("Conten-type: text/html")
print()

os='docker ps --format \"{{.Names}}\"'
status='docker ps --format \"{{.Status}}\"'
image='docker ps --format \"{{.Image}}\"'
osls=(subprocess.getoutput('sudo '+os)).split("\n")
statusls=(subprocess.getoutput('sudo '+status)).split("\n")
imagels=(subprocess.getoutput('sudo '+image)).split("\n")
db={"container":osls,"status":statusls,"image":imagels}
js=json.dumps(db)
print(js)
