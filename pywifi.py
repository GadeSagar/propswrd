import subprocess
import os 
result1 = subprocess.check_output(["netsh", "wlan", "show", "network"])
result1 = result1.decode("ascii")
result1 = result1.replace("\r", "")
ls = results1.split("\n")
ls =  ls[ 4: ]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.appen(ls[x])
    x += 1
print(ssids)
