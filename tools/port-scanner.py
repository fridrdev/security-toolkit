import socket
import sys
from datetime import datetime

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def scan_target(ip, ports):
    print(f"\nScanning {ip}")
    print(f"Started at: {datetime.now()}\n")
    
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            print(f"  [OPEN]   Port {port}")
            open_ports.append(port)
        else:
            print(f"  [closed] Port {port}")
    
    print(f"\n{len(open_ports)} open ports found.")
    return open_ports

common_ports = [21, 22, 23, 25, 53, 80, 443, 3389, 8080]
target = "127.0.0.1" #YOUR_TARGET_IP
scan_target(target, common_ports)
