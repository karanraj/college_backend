#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
osname=cmd.getvalue('osn')
image=cmd.getvalue('im')
myx='docker commit {0} {1}'.format(osname,image)
output=subprocess.getstatusoutput('sudo '+myx)
status=output[0]
cmdout=output[1]
db={"output":cmdout,"status":status}
js=json.dumps(db)
print(js)
