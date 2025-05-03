import socket
import ipaddress
import requests

try:
    from ipwhois import IPWhois
except ImportError:
    IPWhois = None  # ipwhois not installed


def lookup(ip, use_api=True):
    if use_api:
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=3)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"[!] API lookup failed for {ip}: {e}")
            print("[*] Falling back to local lookup...")

    return local_lookup(ip)


def local_lookup(ip):
    info = {
        "ip": ip,
        "hostname": "N/A",
        "city": "N/A",
        "region": "N/A",
        "country": "N/A",
        "org": "N/A",
        "asn": "N/A",
        "loc": "N/A"
    }

    # Validate IP
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        print(f"[!] Invalid IP address: {ip}")
        info["hostname"] = "Invalid IP"
        return info

    # Reverse DNS
    try:
        info["hostname"] = socket.gethostbyaddr(ip)[0]
    except Exception as e:
        print(f"[!] Reverse DNS lookup failed for {ip}: {e}")

    # WHOIS via ipwhois
    if IPWhois:
        try:
            obj = IPWhois(ip)
            data = obj.lookup_rdap()
            info["org"] = data.get("network", {}).get("name", "N/A")
            info["asn"] = data.get("asn", "N/A")
            info["country"] = data.get("network", {}).get("country", "N/A")
        except Exception as e:
            print(f"[!] WHOIS lookup failed for {ip}: {e}")
    else:
        print("[!] ipwhois module not available. Skipping WHOIS lookup.")

    return info
