import socket
import sys
from datetime import datetime

target = input("Enter target IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning {target}...")
print(f"Time: {datetime.now()}")
print("-"*40)

open_ports = []

for port in range(start, end + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"Port {port} OPEN - {service}")
            open_ports.append(port)
        sock.close()
    except KeyboardInterrupt:
        print("\nStopped!")
        sys.exit()
    except:
        pass

print("-"*40)
print(f"Found {len(open_ports)} open ports!")
