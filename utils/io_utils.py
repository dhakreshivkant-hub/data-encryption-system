import struct, socket

HEADER_LEN = 4

def send_with_length(sock: socket.socket, data: bytes) -> None:
    length = len(data)
    sock.sendall(struct.pack("!I", length) + data)

def recv_exact(sock: socket.socket, n: int) -> bytes:
    buf = bytearray()
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise EOFError("Socket closed while reading")
        buf.extend(chunk)
    return bytes(buf)

def recv_length_prefixed(sock: socket.socket) -> bytes:
    hdr = recv_exact(sock, HEADER_LEN)
    (length,) = struct.unpack("!I", hdr)
    return recv_exact(sock, length) if length else b""
