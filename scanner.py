import socket
from datetime import datetime
import threading

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    except Exception:
        pass

def start_scan(target, ports):
    print(f"Starting scan on {target} at {datetime.now()}")
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print("Scan completed")

if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_ports = [21, 22, 80, 443, 8080]
    start_scan(target_host, target_ports)
