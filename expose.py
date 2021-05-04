#!/usr/bin/python3
import subprocess
import json
import cgi
import os
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
osname=cmd.getvalue('osn')
image=cmd.getvalue('im')
storage=cmd.getvalue('st')
bsport=cmd.getvalue('bport')
contport=cmd.getvalue('cport')
net=cmd.getvalue('ntn')
myx='docker run -idt -v {vol} --network {network} -p {baseport}:{container_port} --name {container_name} {img}'.format(vol=storage,network=net,baseport=bsport,container_port=contport,container_name=osname,img=image)
output=subprocess.getstatusoutput('sudo '+myx)
if output[0] == 0:
    os.system("sudo docker exec {0} /usr/sbin/httpd".format(osname))
    print('Container Exposed Sucessfully')
else:
    print(output[1])
status=output[0]
cmdout=output[1]
db={"output":cmdout,"status":status}
js=json.dumps(db)
#subprocess.getoutput("docker exec {0} /usr/sbin/httpd".format(osname))
print(js)
