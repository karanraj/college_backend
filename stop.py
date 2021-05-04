#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
os=cmd.getvalue('osn')
mycmd='docker stop {0}'.format(os)
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
