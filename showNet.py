#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

name = 'docker network ls --format \"{{.Name}}\"'
driver = 'docker network ls --format \"{{.Driver}}\"'
ID = 'docker network ls --format \"{{.ID}}\"'
namels = (subprocess.getoutput('sudo '+name)).split("\n")
driverls = (subprocess.getoutput('sudo '+driver)).split("\n")
IDls = (subprocess.getoutput('sudo '+ID)).split("\n")
db={"name":namels,"driver":driverls,"id":IDls}
js=json.dumps(db)
print(js)
