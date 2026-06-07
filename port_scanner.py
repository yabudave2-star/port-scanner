import nmap
import sys

def banner():
    print("="*50)
    print("   Port Scanner v1.0")
    print("   Powered by python-nmap")
    print("="*50)

def scan(target, scan_type):
    nm = nmap.PortScanner()
    print(f"\n[*] Scanning {target}...")
    print("-"*50)
    
    if scan_type == "1":
        nm.scan(target, arguments="-p 1-1000")
    elif scan_type == "2":
        nm.scan(target, arguments="-sV -p 1-1000")
    elif scan_type == "3":
        nm.scan(target, arguments="-A")
    elif scan_type == "4":
        nm.scan(target, arguments="--script=vuln")

    for host in nm.all_hosts():
        print(f"[+] Host: {host}")
        print(f"[+] State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port].get('product','')
                print(f"    Port {port}/{proto} | {state} | {service} {version}")

def main():
    banner()
    target = input("\n[*] Enter target IP: ")
    print("\n[1] Basic Scan")
    print("[2] Service Scan")
    print("[3] Aggressive Scan")
    print("[4] Vuln Scan")
    choice = input("\n[*] Choose: ")
    scan(target, choice)

if __name__ == "__main__":
    main()
