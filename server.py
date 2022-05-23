from tkinter import *
import socket
import random
import threading



def start_server():
    global tcpSocket
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.bind(("",8000))
    threading._start_new_thread(start_game, ())
    start_btn["state"] = "disable"

def stop_server():
    main_win.destroy()


def start_game():
    count = 0
    while True:
        tcpSocket.listen(1)
        (client, (ip, port)) = tcpSocket.accept()

        print("connect")
        canvas_main.create_text(80, 100+count*25, text=f"client connected", fill="#BDF2F2",
                    font="Times 15 bold",justify="center",anchor=N)
       
        num = random.randint(1, 20)
        print("Random Number is", num)
        canvas_main.create_text(280, 100+count*25, text=f"random is {num}", fill="#BDF2F2",
                    font="Times 15 bold",justify="center",anchor=N)
 


        turn = 0
        count += 1
        while turn <= 5:

            try:
                turn += 1
                data = int(client.recv(2048).decode())
                if int(data) == num:
                    client.send("Win".encode()+str(turn).encode())
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

def hover_in(e):                                                         
    e.widget["background"] = "#85B4F2"


def hover_out(e):                                                         
    e.widget["background"] = "#7EA5F2"


main_win = Tk()
main_win.geometry("350x600")
main_win.resizable(0, 0)
main_win.title("Server Monitor")

canvas_main = Canvas(main_win, width=350, height=600,bg="black")
canvas_main.pack(fill="both", expand=True)
canvas_main.create_text(150, 15, text="Server", fill="#BDF2F2",
                        font="Times 18 bold",justify="center",anchor="n")
start_btn = Button(canvas_main,text="start",command=start_server, bg="#7EA5F2", relief="groove",
                activebackground="#85B4F2")
stop_btn = Button(canvas_main,text="stop",command=stop_server, bg="#7EA5F2", relief="groove",
                activebackground="#85B4F2")


start_btn.place(x=125,y=50,anchor=NE)
start_btn.bind("<Enter>", hover_in)
start_btn.bind("<Leave>", hover_out)

stop_btn.place(x=175,y=50,anchor=NW)
stop_btn.bind("<Enter>", hover_in)
stop_btn.bind("<Leave>", hover_out)

main_win.mainloop()