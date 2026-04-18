import socket

def scan_port(target, port):
    """Return True if the port is open, otherwise False."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # wait up to 1 second
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        return False
    except socket.error:
        print("Error: Could not connect to the server.")
        return False

def main():
    print("Simple Python Port Scanner")
    print("-" * 30)

    target = input("Enter an IP address or hostname to scan: ").strip()

    # Common ports for a beginner project
    ports_to_scan = range(20,1025)

    print(f"\nScanning {target}...\n")

    for port in ports_to_scan:
        is_open = scan_port(target, port)
        if is_open:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

if __name__ == "__main__":
    main()