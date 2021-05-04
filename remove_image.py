#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
image=cmd.getvalue('img')
mycmd='docker image rm {0}'.format(image)
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
