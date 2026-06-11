import os

SIGNATURE_FILE = "virus_signatures.txt"

# Load malware signatures
def load_signatures():
    try:
        with open(SIGNATURE_FILE, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print("[ERROR] Signature database not found.")
        return []

# Scan a file
def scan_file(filepath, signatures):
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read().lower()

        for signature in signatures:
            if signature.lower() in content:
                return True, signature

        return False, None

    except Exception as e:
        print(f"Error scanning {filepath}: {e}")
        return False, None

# Scan folder
def scan_folder(folder):
    signatures = load_signatures()

    if not signatures:
        return

    infected_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            infected, sig = scan_file(path, signatures)

            if infected:
                infected_files.append((path, sig))
                print(f"[INFECTED] {path} -> Signature: {sig}")
            else:
                print(f"[CLEAN] {path}")

    print("\n===== Scan Summary =====")

    if infected_files:
        print(f"Detected {len(infected_files)} infected files")
    else:
        print("No threats found")

if __name__ == "__main__":
    target_folder = input("Enter folder path to scan: ")
    scan_folder(target_folder)