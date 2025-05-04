import socket
from rich import print

// Port checking function
def check_port(target, port):
    try:
        // Mapping port to its name
        service_name = socket.getservbyport(port)
        // Handling non existing port
    except (OSError, OverflowError):
        print(f"[bold red]Port {port} is not valid.[/]")
        return None
    // Creating a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        // Connecting to the socket on a target (eg: 192.168.0.110)
        r = s.connect_ex((target, port))

        print()
        print("="*50)
        print(f"Checking Port: [bold blue]{port}/{service_name}[/] on [bold yellow]{target}[/]")
        print("="*50)

        if r == 0:
            print(f"Status: [bold green]Open[/]")
        else:
            print(f"Status: [bold red]Filtered[/] | [bold red]Closed[/]")

        print("="*50)
        print()

def check_ports(target, start_port, end_port):
    try:
        if start_port > end_port or target == "":
            raise ValueError("There was an error in either 'target', 'start_port' or 'end_port'")
        for port in range(start_port, end_port + 1):
            check_port(target, port) 
    except ValueError as error:
        print(f"[bold red]{error.args[0]}[/]")

check_ports("127.0.0.1", 19, 80)
