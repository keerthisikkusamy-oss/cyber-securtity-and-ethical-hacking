import requests

target = "http://example.com"

wordlist = [
    "admin",
    "login",
    "uploads",
    "images",
    "backup",
    "config",
    "api"
]

print(f"Scanning {target}...\n")

for directory in wordlist:
    url = f"{target}/{directory}/"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"[FOUND] {url}")
        elif response.status_code == 403:
            print(f"[FORBIDDEN] {url}")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"[REDIRECT] {url}")
        else:
            print(f"[{response.status_code}] {url}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {url} - {e}")