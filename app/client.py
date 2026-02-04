import time
import tkinter
import threading
import socket
from tkinter import *
from tkinter import messagebox


def ZoviServer():
    if (len(ime_vr.get()) == 0 or len(prezime_vr.get()) == 0 or len(adresa_vr.get()) == 0 or len(
            brtelefona_vr.get()) < 10 or obim.get() == 0 or placanje.get() == 0):
        messagebox.showerror("Greska", "Molim vas proverite da li su sva polja popunjena!")
    else:
        s = socket.socket()
        host = socket.gethostname()
        port = 12345
        s.connect((host, port))
        a = ""
        b = ""
        c = ""
        d = ""
        e = ""
        if (kecap.get() == True):
            a = "Kecap"
        if (majonez.get() == True):
            b = "Majonez"
        if (origano.get() == True):
            c = "Origano"
        if (obim.get() == 1):
            d = "25cm"
        elif (obim.get() == 2):
            d = "32cm"
        elif (obim.get() == 3):
            d = "50cm"
        if (placanje.get() == 1):
            e = "Gotovina"
        elif (placanje.get() == 2):
            e = "Kartica"
        poruka = ime_vr.get() + " " + prezime_vr.get() + "," + adresa_vr.get() + "," + brtelefona_vr.get() + "," + napomena_vr.get() + \
                 "," + str(listbox1.get('active')) + "," + a + " " + b + " " + c + "," + d + "," + e
        s.send(poruka.encode())
        prijem = (s.recv(1024)).decode()
        messagebox.showinfo("Vreme isporuke", str(prijem))
        s.close()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)


root = Tk()
root.geometry("235x635")
srednji_okvir = Frame(root)
srednji_okvir.pack(anchor=CENTER)
Label(srednji_okvir, text="Narucite pizzu:", font=("Tahoma", "18")).pack(side=TOP)
Label(srednji_okvir, text="Ime:").pack(side=TOP)
ime_vr = StringVar()
e1 = Entry(srednji_okvir, textvariable=ime_vr)
e1.pack(side=TOP)
prezime_vr = StringVar()
brtelefona_vr = StringVar()
adresa_vr = StringVar()
napomena_vr = StringVar()
Label(srednji_okvir, text="Prezime:").pack(side=TOP)
e2 = Entry(srednji_okvir, textvariable=prezime_vr)
e2.pack(side=TOP)
Label(srednji_okvir, text="Adresa:").pack(side=TOP)
e3 = Entry(srednji_okvir, textvariable=adresa_vr)
e3.pack(side=TOP)

Label(srednji_okvir, text="Broj telefona:").pack(side=TOP)
e4 = Entry(srednji_okvir, textvariable=brtelefona_vr)
e4.pack(side=TOP)

Label(srednji_okvir, text="Napomena:").pack(side=TOP)
e5 = Entry(srednji_okvir, textvariable=napomena_vr)
e5.pack(side=TOP)
Label(srednji_okvir, text="Izaberite pizzu:").pack(side=TOP)
listbox1 = Listbox(srednji_okvir, selectmode=SINGLE, height=5)
listbox1.insert(0, "Vegetariana")
listbox1.insert(1, "Capricciosa")
listbox1.insert(2, "Quatro Stagione")
listbox1.insert(3, "Fungi")
listbox1.insert(4, "Prsuto")
listbox1.select_set(0, 0)
listbox1.pack(side=TOP)

kecap = BooleanVar()
majonez = BooleanVar()
origano = BooleanVar()

Label(srednji_okvir, text="Prilozi:", bg="Blue", fg="White").pack(side=TOP)
Checkbutton(srednji_okvir, text="Kecap", variable=kecap, onvalue=True, offvalue=False).pack(side=TOP)
Checkbutton(srednji_okvir, text="Majonez", variable=majonez, onvalue=True, offvalue=False).pack(side=TOP)
Checkbutton(srednji_okvir, text="Origano", variable=origano, onvalue=True, offvalue=False).pack(side=TOP)
obim = IntVar()
placanje = IntVar()
Label(srednji_okvir, text="Obim:", bg="Blue", fg="White").pack(side=TOP)
Radiobutton(srednji_okvir, text="25cm", variable=obim, value=1).pack(side=TOP)
Radiobutton(srednji_okvir, text="32cm", variable=obim, value=2).pack(side=TOP)
Radiobutton(srednji_okvir, text="50cm", variable=obim, value=3).pack(side=TOP)
Label(srednji_okvir, text="Nacin placanja:", bg="Blue", fg="White").pack(side=TOP)
Radiobutton(srednji_okvir, text="Gotovina", variable=placanje, value=1).pack(side=TOP)
Radiobutton(srednji_okvir, text="Kartica", variable=placanje, value=2).pack(side=TOP)
Button(srednji_okvir, text="Naruci", command=ZoviServer, width=25).pack(side=BOTTOM)

root.resizable(0, 0)
root.title("Pizza Client")
root.mainloop()