import socket
import random

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind(("",8000))

while True:
    tcpSocket.listen(1)
    (client, (ip, port)) = tcpSocket.accept()
    print("connect")

    num = random.randint(1, 20)
    print("Random Number is", num)
    turn = 0
    while turn <= 5:

        try:
            turn += 1
            data = int(client.recv(2048).decode())
            if int(data) == num:
                client.send("win".encode()+str(turn).encode())
                break
            if int(data) > num:
                if turn == 5:
                    client.send("Lost".encode() + str(turn).encode())
                    break
                else:
                    client.send("High".encode()+str(turn).encode())
            if int(data) < num:
                if turn == 5:
                    client.send("Lost".encode() + str(turn).encode())
                    break
                else:
                    client.send("Low".encode() + str(turn).encode())
        except ValueError:
            break
        print("Turn taken", turn)


