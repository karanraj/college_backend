#!/usr/bin/python3
import subprocess as sp
import cgi

print("Conten-type: text/html\n")

cmd=cgi.FieldStorage()
ip=cmd.getvalue('ip')
usr=cmd.getvalue('usr')
passd=cmd.getvalue('pass')

out=sp.getstatusoutput("echo \'{0} ansible_remote_user={1} ansible_ssh_pass={2}\' >> /Ansible_WorkStation/Local/hosts".format(ip,usr,passd))

if out[0]==0:
    print("done")
else:
    print(out[1])
