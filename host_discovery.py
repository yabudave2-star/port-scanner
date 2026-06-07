import socket
import subprocess

ip = input("Enter IP: ")

first = int(ip.split(".")[0])

if 1 <= first <= 126:
    c = "Class A"
elif 128 <= first <= 191:
    c = "Class B"
elif 192 <= first <= 223:
    c = "Class C"
elif 224 <= first <= 239:
    c = "Class D"
else:
    c = "Class E"

result = subprocess.run("ipconfig", capture_output=True, text=True)
gateway = "Not found"
for line in result.stdout.split("\n"):
    if "Default Gateway" in line:
        g = line.split(":")[-1].strip()
        if g:
            gateway = g
            break

print("IP:", ip)
print("Class:", c)
print("Gateway:", gateway)
