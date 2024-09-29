import tkinter as tk
from tkinter import PhotoImage


ventana = tk.Tk() #La segunda T va en mayuscula



ventana.title("Mi primer ventana") #Cambia el nombre de la ventana
ventana.geometry("600x400+1000+1000") #Cambia el tamaño de la ventana, +0 +0 es la posicion inicial
ventana.minsize(400, 200) #Cambia el tamaño minimo de la ventana, primero recibe el ancho y luego el alto
ventana.maxsize(800, 600)

img = PhotoImage(file="perro.png")
ventana.iconphoto(False, img)

ventana.configure(bg="dodgerblue2")

ventana.resizable(False, True) #Cambia el tamaño de la ventana, el primer True es el ancho y el segundo el alto, para mover la ventana
ventana.attributes("-alpha", 0.6) #Cambia la opacidad de la ventana

ventana.mainloop() #Mantiene la ventana abierta




