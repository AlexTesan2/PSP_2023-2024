import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Settimeout para evitar errores

        try:
            sock.connect((ip, port))
            open_ports.append(port)
            print(f"Port {port} is open")
        except (socket.timeout, socket.error):
            print(f"Port {port} is closed")
            pass
        finally:
            sock.close()

    return open_ports

def main():
    ip_address = input("Enter the IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    open_ports = scan_ports(ip_address, start_port, end_port)

    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
