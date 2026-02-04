import socket
import tkinter
from tkinter import *
import threading
import random
import time

brojac = 0
brojac_2 = 0
narudzbine = []


def fja():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    global brojac
    data = []
    while True:
        conn, addr = s.accept()
        print("Connection from: ", addr)
        data = conn.recv(1024).decode().split(",")
        vreme = random.randint(10, 51)
        vremesek = vreme * 60
        poruka = data[0] + " | " + data[1] + " | " + data[2] + " | " + data[3] + " | " + data[4] + " | " + data[
            5] + " | " + data[6] + " | " + data[7] + " |"
        conn.send(("Vreme isporuke: " + str(vreme) + " minuta.").encode())
        listbox1.insert(brojac, poruka)
        narudzbine.insert(brojac, [brojac, vremesek])
        conn.close()
        brojac += 1
        print(narudzbine)


def smanjiVreme():
    global brojac_2

    while True:
        sek = 1
        if (len(narudzbine) > 0):
            sek = 1 / len(narudzbine)
        # print("Radim")
        if (listbox1.size() > 0):
            for index in range(len(narudzbine)):
                if (narudzbine[index][1] == 0):
                    listbox2.insert(brojac_2, listbox1.get(index)[:-len(str(narudzbine[index][1]))])
                    listbox1.delete(index)
                    brojac_2 += 1
                    narudzbine[index][1] = -1
                    del narudzbine[index]
                    listbox3.delete(index)
                    break
                elif (narudzbine[index][1] > 0):
                    print(narudzbine[index][1])
                    temp = listbox1.get(index)
                    print(len(str(narudzbine[index][1])))
                    listbox3.delete(index)
                    listbox3.insert(index, str(narudzbine[index][1]))
                    narudzbine[index][1] -= 1
                    time.sleep(sek)
        time.sleep(0.01)


root = tkinter.Tk()
root.geometry("585x540")

neisporucene = Frame(root)
neisporucene.grid(row=0, column=0)
Label(neisporucene, text="Neisporucene porudzbine:", bg="Red", fg="White").pack()
listbox1 = Listbox(neisporucene, selectmode=SINGLE, height=15, width=90)
listbox1.select_set(0, 0)
listbox1.pack()

vreme = Frame(root)
vreme.grid(row=0, column=1)
Label(vreme, text="Vreme:", bg="Purple", fg="White").pack()
listbox3 = Listbox(vreme, selectmode=SINGLE, height=15, width=6)
listbox3.select_set(0, 0)
listbox3.pack()

isporucene = Frame(root)
isporucene.grid(row=1, column=0)
Label(isporucene, text="Isporucene porudzbine:", bg="Green", fg="White").pack()
listbox2 = Listbox(isporucene, selectmode=SINGLE, height=15, width=90)
listbox2.select_set(0, 0)
listbox2.pack()

t1 = threading.Thread(target=fja).start()
t2 = threading.Thread(target=smanjiVreme).start()
root.resizable(0, 0)
root.title("Pizza Server")
root.mainloop()