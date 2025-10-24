# tiny_honeypot.py — educational only
# Listens on a port, logs remote IP + data received (no execution).
import socket
import datetime
import logging

logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

HOST = '0.0.0.0'
PORT = 2222  # pick an unused port (e.g., mimic SSH 2222)

def now(): return datetime.datetime.utcnow().isoformat() + 'Z'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    logging.info(f"[{now()}] Honeypot listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            peer = f"{addr[0]}:{addr[1]}"
            logging.info(f"[{now()}] Connection from {peer}")
            try:
                conn.settimeout(5.0)
                data = conn.recv(4096)
                if data:
                    logging.info(f"[{now()}] Data from {peer}: {data[:400]!r}")
                # respond with a fake banner to keep attackers engaged
                banner = b"SSH-2.0-OpenSSH_7.4p1 Ubuntu-10\r\n"
                conn.sendall(banner)
            except socket.timeout:
                logging.info(f"[{now()}] Timeout from {peer}")
            except Exception as e:
                logging.exception(f"[{now()}] Error: {e}")
