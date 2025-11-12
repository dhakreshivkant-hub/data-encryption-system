#!/usr/bin/env python3
import argparse, json, os, socket
from utils.crypto_utils import load_key
from utils.io_utils import send_with_length

def send_file(host, port, key_path, file_path):
    fernet = load_key(key_path)
    filesize = os.path.getsize(file_path)
    filename = os.path.basename(file_path)
    header = json.dumps({"filename": filename, "filesize": filesize}).encode("utf-8")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        send_with_length(s, header)
        with open(file_path, "rb") as f:
            while chunk := f.read(65536):
                enc = fernet.encrypt(chunk)
                send_with_length(s, enc)
        send_with_length(s, b"")
    print("File sent successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=9000)
    parser.add_argument("--key", required=True)
    parser.add_argument("--file", required=True)
    args = parser.parse_args()
    send_file(args.host, args.port, args.key, args.file)
