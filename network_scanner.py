import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter Target IP Address: ")

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    except:
        pass

print(f"\nScanning {target}...\n")

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, ports)

print("\nScan Complete!")
