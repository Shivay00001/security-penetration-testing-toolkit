import argparse
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

def parse_ports(spec):
    """Parse '22,80,443' or '20-25' into a list of ints."""
    ports = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            ports.update(range(int(lo), int(hi) + 1))
        elif part:
            ports.add(int(part))
    return sorted(ports)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Security Penetration Testing Toolkit - multithreaded TCP port scanner."
    )
    parser.add_argument("--target", default="127.0.0.1",
                        help="Target host or IP to scan (default: 127.0.0.1)")
    parser.add_argument("--ports", default="21,22,80,443,8080",
                        help="Ports to scan, e.g. '22,80,443' or '20-100' (default: 21,22,80,443,8080)")
    args = parser.parse_args()
    start_scan(args.target, parse_ports(args.ports))
