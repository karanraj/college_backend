#!/usr/bin/python3
import subprocess

print("content-type: text/html")
print()
c=subprocess.getoutput("cal")
print(c)
