import re

# Sample phishing indicators
suspicious_keywords = [
    "urgent",
    "verify your account",
    "account suspended",
    "click here",
    "password",
    "bank details",
    "login immediately",
    "security alert"
]

# Sample email content
email_text = """
Dear Customer,

Your account has been suspended.
Please click here to verify your account immediately:

http://secure-bank-login.xyz

Failure to act within 24 hours will result in permanent closure.

Regards,
Support Team
"""

score = 0

# Check for phishing keywords
for keyword in suspicious_keywords:
    if keyword.lower() in email_text.lower():
        print(f"[!] Suspicious keyword found: {keyword}")
        score += 1

# Find URLs
urls = re.findall(r'https?://[^\s]+', email_text)

for url in urls:
    print(f"[+] URL Found: {url}")

    if ".xyz" in url or "login" in url:
        print("[!] Suspicious URL detected")
        score += 2

print("\n------ Analysis Result ------")

if score >= 3:
    print("⚠ Potential Phishing Email Detected")
else:
    print("✓ Email appears relatively safe")

print(f"Risk Score: {score}")