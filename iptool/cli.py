import argparse
from rich.console import Console
from rich.table import Table
from iptool.iplookup import lookup

def main():
    console = Console()

    parser = argparse.ArgumentParser(description="IP Lookup Tool")
    parser.add_argument("ips", nargs="*", help="One or more IP addresses")
    parser.add_argument("--no-api", action="store_true", help="Use local lookup only (no external API)")

    args = parser.parse_args()

    if not args.ips:
        console.print("[bold red]Error:[/bold red] No IPs provided.\n")
        console.print("Usage:")
        console.print("  [green]python run.py 8.8.8.8[/green]")
        console.print("  [green]python run.py --no-api 1.1.1.1 8.8.4.4[/green]")
        return

    for ip in args.ips:
        data = lookup(ip, use_api=not args.no_api)

        table = Table(title=f"Info for {ip}")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")

        for field in ["ip", "hostname", "city", "region", "country", "org", "asn", "loc"]:
            table.add_row(field.capitalize(), data.get(field, "N/A"))

        console.print(table)

if __name__ == "__main__":
    main()
