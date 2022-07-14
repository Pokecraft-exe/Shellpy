import requests
import time
import os
requests.urllib3.disable_warnings()

def tryUpdate():
    print("updating... please wait...")
    try:
        os.remove("shell.py")
        with open('shell.py', 'wb') as f:
            f.write(requests.get("https://raw.githubusercontent.com/Pokecraft-exe/Shellpy/main/shell.py").content)
    except:
        return 1
    return 0

a = 1
while a == 1:
    a = tryUpdate()
    print("Error, verify your internet connexion. we are trying again...")
    time.sleep(0.5)
    tryUpdate()
print("done")
time.sleep(1)
