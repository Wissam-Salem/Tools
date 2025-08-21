import socket
from rich import print

# Port checking function
def check_port(target: str, port: int):
    try:
        # Mapping port to its name
        service_name = socket.getservbyport(port)
    # Handling non existing port
    except (OSError, OverflowError):
        print(f"[bold red]Port {port} is not reachable.[/]")
        return None
    # Creating a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2.0)
        # Connecting to the socket on a target (eg: 192.168.0.110)
        r = s.connect_ex((target, port))

        print()
        print("="*50)
        print(f"Checking Port: [bold blue]{port}/{service_name}[/] on [bold yellow]{target}[/]")
        print("="*50)
        with open(file=f"ports_status_{target}.txt", mode="a", encoding="utf-8") as file:
            if r == 0:
                print(f"Status: [bold green]Open[/]")
                file.write(f"tcp/{port} ({service_name}) --> open\n")
            else:
                print(f"Status: [bold red]Filtered[/] | [bold red]Closed[/]")
                file.write(f"tcp/{port} ({service_name}) --> closed/filtered\n")

        print("="*50)
        print()

def check_ports(target, start_port, end_port):
    try:
        if start_port > end_port or target == "":
            raise ValueError("There was an error in either 'target', 'start_port' or 'end_port'.")
        for port in range(start_port, end_port + 1):
            check_port(target, port) 
    except ValueError as error:
        print(f"[bold red]{error.args[0]}[/]")

check_ports("localhost", 19, 80)
