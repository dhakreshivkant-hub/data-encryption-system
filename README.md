# Data Encryption File Transfer

Simple encrypted file transfer using cryptography.Fernet for symmetric authenticated encryption.

## Requirements
- Python 3.8+
- pip

## Install
```
pip install -r requirements.txt
```

## Usage
1. Generate a key:
```
python generate_key.py key.key
```

2. Start server:
```
python server.py --host 0.0.0.0 --port 9000 --key key.key
```

3. Send file:
```
python client.py --host SERVER_IP --port 9000 --key key.key --file example_files/sample.txt
```

The server writes the received file to its current directory.

## Notes
This example uses a pre-shared symmetric key (Fernet). For production use, prefer TLS or asymmetric key exchange.
