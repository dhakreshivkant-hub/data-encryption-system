#!/usr/bin/env python3
from cryptography.fernet import Fernet
import sys

def main(path: str):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    print(f"Wrote key to {path}. Transfer securely.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_key.py key.key")
        sys.exit(1)
    main(sys.argv[1])
