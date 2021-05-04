#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
image=cmd.getvalue('img')
version=cmd.getvalue('ver')
mycmd='docker pull {0}:{1}'.format(image,version)
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
