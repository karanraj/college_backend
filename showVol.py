#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

driver = 'docker volume ls --format \"{{.Driver}}\"'
name = 'docker volume ls --format \"{{.Name}}\"'
driverls = (subprocess.getoutput('sudo '+driver)).split("\n")
namels = (subprocess.getoutput('sudo '+name)).split("\n")
db={"driver":driverls,"name":namels}
js=json.dumps(db)
print(js)
