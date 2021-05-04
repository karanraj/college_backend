#!/usr/bin/python3
import subprocess

print("content-type: text/html")
print()
d=subprocess.getoutput("date")
print(d)
