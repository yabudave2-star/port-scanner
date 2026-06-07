import nmap
import sys

nm = nmap.PortScanner()

target = input("Enter target IP: ")
print("\n[1] Basic Scan")
print("[2] Service Scan")
print("[3] Aggressive Scan")
choice = input("\nChoose: ")

print(f"\nScanning {target}...")

if choice == "1":
    nm.scan(target, arguments="-p 1-1000")
elif choice == "2":
    nm.scan(target, arguments="-sV -p 1-1000")
elif choice == "3":
    nm.scan(target, arguments="-A")

for host in nm.all_hosts():
    print(f"\nHost: {host}")
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in sorted(ports):
            state = nm[host][proto][port]['state']
            service = nm[host][proto][port]['name']
            print(f"Port {port} {state} {service}")
