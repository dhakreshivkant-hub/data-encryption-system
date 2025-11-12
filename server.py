#!/usr/bin/env python3
import argparse, json, os, socket
from utils.io_utils import recv_length_prefixed
from utils.crypto_utils import load_key

def handle_client(conn, fernet):
    try:
        header_bytes = recv_length_prefixed(conn)
        header = json.loads(header_bytes.decode("utf-8"))
        filename = os.path.basename(header["filename"])
        with open(filename, "wb") as out_f:
            while True:
                enc_chunk = recv_length_prefixed(conn)
                if enc_chunk == b"":
                    break
                plain = fernet.decrypt(enc_chunk)
                out_f.write(plain)
        print(f"Received {filename}")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def run_server(host, port, key_path):
    fernet = load_key(key_path)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print(f"Listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            print("Connection from", addr)
            handle_client(conn, fernet)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=9000)
    parser.add_argument("--key", required=True)
    args = parser.parse_args()
    run_server(args.host, args.port, args.key)
