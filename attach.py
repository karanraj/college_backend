#!/usr/bin/python3
import subprocess
import json
import cgi
#print("Conten-type: text/html")
#print()

#cmd=cgi.FieldStorage()
#osname=cmd.getvalue('osn')
#image=cmd.getvalue('im')
#storage=cmd.getvalue('st')
#net=cmd.getvalue('ntn')
myx='docker build -t mycentos:v1 /var/www/cgi-bin/'
output=subprocess.getoutput('sudo '+myx)
#status=output[0]
#cmdout=output[1]
#db={"output":cmdout,"status":status}
#js=json.dumps(db)
print(output)
