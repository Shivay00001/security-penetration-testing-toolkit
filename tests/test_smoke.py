"""Minimal smoke test for security-penetration-testing-toolkit (stdlib-only)."""
import os
import socket
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import scanner


def test_scan_port_closed_port_no_exception():
    # Port 1 on localhost is (almost) certainly closed; scan must not raise.
    scanner.scan_port("127.0.0.1", 1)


def test_scan_port_open_port_no_exception():
    # Open a real listening socket, scan it, ensure no exception.
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    try:
        scanner.scan_port("127.0.0.1", port)
    finally:
        srv.close()


def test_start_scan_empty_port_list():
    scanner.start_scan("127.0.0.1", [])
