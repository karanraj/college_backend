#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
driver=cmd.getvalue('drive')
netname=cmd.getvalue('net')
mycmd='docker network create --driver {0} {1}'.format(driver,netname)
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
