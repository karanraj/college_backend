#!/usr/bin/python3
import subprocess
import json
import cgi
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
osname=cmd.getvalue('osn')
image=cmd.getvalue('im')
#storage=cmd.getvalue('st')
ntwrk=cmd.getvalue('ntn')
if "bridge" in ntwrk:
    net="bridge"
else:
    net="bridge"
myx='docker run -dit --network {0} -P --name {1} {2}'.format(net,osname,image)
output=subprocess.getstatusoutput('sudo '+myx)
status=output[0]
cmdout=output[1]
db={"output":cmdout,"status":status}
js=json.dumps(db)
print(js)
