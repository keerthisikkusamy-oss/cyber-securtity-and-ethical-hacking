import requests

def analyze_api(url):
    try:
        response = requests.get(url, timeout=10)

        print(f"\n[*] URL: {url}")
        print(f"[*] Status Code: {response.status_code}")

        print("\n=== Security Headers ===")
        headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Access-Control-Allow-Origin"
        ]

        for header in headers:
            value = response.headers.get(header)
            if value:
                print(f"[+] {header}: {value}")
            else:
                print(f"[-] Missing: {header}")

        print("\n=== Server Information ===")
        if "Server" in response.headers:
            print(f"Server: {response.headers['Server']}")
        else:
            print("Server header hidden")

        print("\n=== Response Preview ===")
        print(response.text[:300])

    except Exception as e:
        print("Error:", e)

target = input("https://catfact.ninja/facts: ")
analyze_api(target)