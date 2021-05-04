#!/usr/bin/python3
import subprocess
import json
print("Conten-type: text/html")
print()

mycmd='docker container rm $(docker container ls -aq)'
output=subprocess.getstatusoutput('sudo '+mycmd)
status=output[0]
cmdoutput=output[1]
db={"output":cmdoutput,"status":status}
js=json.dumps(db)
print(js)
