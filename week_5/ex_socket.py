# создание сокета, таймауты и обработка ошибок
# сервер
import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        conn.settimeout(5)  # timeout := None|0|gt 0 
        with conn:
            while True:
                try:
                    data = conn.recv(1024)

                except socket.timeout:
                    print("close connection by timeout")
                    break

                if not data:
                    break
                # sock.sendall(b"ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n")
                print(data.decode("utf8"))