import subprocess as sp

myx='docker images --format \"{{.Repository}}\"'
output=(sp.getoutput('sudo '+myx)).split("\n")
print(output[0])


