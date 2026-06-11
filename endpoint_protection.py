import os
import json
import hashlib
from datetime import datetime

MONITOR_DIR = r"D:\protected_files"
BASELINE_FILE = "baseline.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception:
        return None


def create_baseline():
    baseline = {}

    for root, dirs, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            baseline[path] = calculate_hash(path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("[+] Baseline created.")


def check_integrity():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_files = {}

    for root, dirs, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            current_files[path] = calculate_hash(path)

    print("\n=== Endpoint Protection Scan ===")

    # Modified files
    for file_path, old_hash in baseline.items():

        if file_path not in current_files:
            print(f"[ALERT] File Deleted: {file_path}")
            continue

        if current_files[file_path] != old_hash:
            print(f"[ALERT] File Modified: {file_path}")

    # New files
    for file_path in current_files:
        if file_path not in baseline:
            print(f"[ALERT] New File Detected: {file_path}")

    print(f"\nScan Time: {datetime.now()}")


if not os.path.exists(BASELINE_FILE):
    create_baseline()
else:
    check_integrity()