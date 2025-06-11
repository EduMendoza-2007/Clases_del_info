import tkinter as tk
import time

ventana = tk.Tk()
ventana.geometry("600x200")
ventana.minsize(200, 100)#Tamanio minimo
ventana.maxsize(600, 200)#Tamanio maximo
ventana.wm_attributes(alpha=0.9)#Transparencia
ventana.configure(bg="Blue")#Color de ventana
ventana.resizable(False, False)#si nos deja modificar o no el ancho y la altura
                 # ancho, alto
ventana.title("Reloj")#titulo de la ventana
#ventana.iconbitmap(ruta de mi imagen)

reloj = tk.Label(ventana, font=("Arial", 90), bg="Black", fg="Red")


def hora():

    tiempo_actual = time.strftime("%H:%M:%S")
    reloj.config(text=tiempo_actual)

#   esta ventana.after() sirve para que se vaya actualizando la hora y no quede fija en cierto tiempo
    ventana.after(1000, hora)#aca en programacion se utilizan los milisegundos


reloj.pack()
hora()
ventana.mainloop()