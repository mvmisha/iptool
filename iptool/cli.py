import sys
from rich.console import Console
from rich.table import Table
from iptool.iplookup import lookup

def main():
    console = Console()
    if len(sys.argv) < 2:
        console.print("[red]Please provide at least one IP address.[/red]")
        return

    for ip in sys.argv[1:]:
        data = lookup(ip)
        table = Table(title=f"Info for {ip}")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")

        for field in ["ip", "hostname", "city", "region", "country", "org", "loc"]:
            table.add_row(field.capitalize(), data.get(field, "N/A"))

        console.print(table)

if __name__ == "__main__":
    main()
