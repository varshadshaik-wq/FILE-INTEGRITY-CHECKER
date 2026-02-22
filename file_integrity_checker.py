import hashlib
import os
import json

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def scan_directory(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            hashes[path] = calculate_hash(path)
    return hashes

def save_hashes(hashes):
    with open("file_hashes.json", "w") as file:
        json.dump(hashes, file, indent=4)

def load_hashes():
    if not os.path.exists("file_hashes.json"):
        return {}
    with open("file_hashes.json", "r") as file:
        return json.load(file)

def check_integrity(directory):
    old_hashes = load_hashes()
    new_hashes = scan_directory(directory)

    print("\nFILE INTEGRITY REPORT\n")

    for file in new_hashes:
        if file not in old_hashes:
            print("NEW FILE:", file)
        elif new_hashes[file] != old_hashes[file]:
            print("MODIFIED FILE:", file)

    for file in old_hashes:
        if file not in new_hashes:
            print("DELETED FILE:", file)

    save_hashes(new_hashes)
    print("\nIntegrity check completed.")

if __name__ == "__main__":
    folder = input("Enter folder path to monitor: ")
    check_integrity(folder)