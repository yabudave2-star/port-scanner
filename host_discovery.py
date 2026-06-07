import socket
import subprocess

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

result = subprocess.run("ipconfig", capture_output=True, text=True)
gateway = "Not found"
for line in result.stdout.split("\n"):
    if "Default Gateway" in line:
        g = line.split(":")[-1].strip()
        if g:
            gateway = g

first = int(ip.split(".")[0])
if 1 <= first <= 126:
    ip_class = "Class A"
elif 128 <= first <= 191:
    ip_class = "Class B"
else:
    ip_class = "Class C"

print("Your IP:", ip)
print("Gateway:", gateway)
print("IP Class:", ip_class)