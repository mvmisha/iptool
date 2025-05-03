import requests

def lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    return response.json()
