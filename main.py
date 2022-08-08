from tkinter import *
import socket
from time import sleep
from turtle import bgcolor


root = Tk()
root.title("TryPort")
root.geometry("320x75")
root.resizable(0,0)

ip = StringVar()
port = StringVar()


etiqueta = Label(root, text="IP").place(x=25, y=15)
entrada1 = Entry(root, textvariable=ip).place(x= 40,y=15)
etiqueta1 = Label(root, text="PORT").place(x=175, y=15)
entrada2 = Entry(root, textvariable=port, width=10).place(x=210,y=15)
etiqueta2 = Label(root, text="By Fede Indrunas").place(x=220, y=55)

def prueba(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(2)
  result = sock.connect_ex((ip,int(port)))
  sock.close()  
  if result == 0:
    return True
  else:
    return False

def press():
  try:
    lbl.destroy()
  except:
    pass
  if prueba(ip.get(),port.get()):
    lbl = Label(root, text="   OK   ", bg="green", font=("Arial Black", 15)).place(x=80, y=40)
    sleep(2)
  else:
    lbl = Label(root, text="   NO   ", bg="red", font=("Arial Black", 15)).place(x=80, y=40)
    sleep(2)

boton = Button(root, text="Probar", command=press).place(x=10, y=45)

if __name__ == "__main__":
  root.mainloop()