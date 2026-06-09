import requests

# Target application login URL
LOGIN_URL = "https://example.com/login"

# Test credentials
username = "testuser"
password = "Password123!"

# Login request data
data = {
    "username": username,
    "password": password
}

try:
    session = requests.Session()

    response = session.post(
        LOGIN_URL,
        data=data,
        timeout=10
    )

    print(f"Status Code: {response.status_code}")

    # Example checks
    if response.status_code == 200:
        if "Welcome" in response.text:
            print("[+] Authentication successful")
        elif "Invalid credentials" in response.text:
            print("[-] Authentication failed")
        else:
            print("[?] Authentication result unclear")
    else:
        print(f"[-] Unexpected response: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")