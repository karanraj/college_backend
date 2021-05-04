#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
volname=cmd.getvalue('vname')
mycmd='docker volume create {0}'.format(volname)
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
