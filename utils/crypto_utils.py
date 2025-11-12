from cryptography.fernet import Fernet

def load_key(path: str) -> Fernet:
    with open(path, "rb") as f:
        key = f.read()
    return Fernet(key)
