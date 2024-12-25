import socket, argparse, os

def Scanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = s.connect_ex((ip, port))
    if data == 0:
        print(f'The Port {port} is open')
    else:
        print(f'The Port {port} is closed')
    s.close()

def PortRange(ip, start_port, end_port):
    print(f"Scanning the IP Address {ip} from {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        Scanner(ip, port)

def Options():
    perser = argparse.ArgumentParser(description="Simple Port Scanner")
    perser.add_argument('IP', help='IP Address')
    perser.add_argument('-o', help='Output save in txt format')
    perser.add_argument('-w', help='Create a Directory and save')
    perser.add_argument('-r', help='Give a range of port number')
    args = perser.parse_args()
    
    ip = args.IP
    port_range = args.r.split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])
    
    Scan_Result = PortRange(ip, start_port, end_port)

    output_dir = 'scan_results'
    if not os.path.exists(output_dir):
            os.mkdir(output_dir)
    
    output_file = os.path.join(output_dir, args.o)
    f = open(output_file, 'w')
    f.writelines(Scan_Result)
    f.close()
    print(f'Your Scan result save to {output_file}')
    
Options()


