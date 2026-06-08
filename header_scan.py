import requests

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)

        headers_to_check = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy"
        ]

        print(f"\nScanning: {url}\n")

        for header in headers_to_check:
            if header in response.headers:
                print(f"[OK] {header}: {response.headers[header]}")
            else:
                print(f"[WARN] Missing header: {header}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter URL (e.g. https://google.com): ")
    check_security_headers(target)