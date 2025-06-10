import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Menu desplegable")
ventana.geometry("400x200")


#Crear un menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Principal", menu=menu_principal)

submenu = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Opciones", menu=submenu)
def mostrar_mensaje():
    print("Hola desde la terminal")
button = tk.Button(ventana, text="Boton saludar", command=mostrar_mensaje)
button.pack()

#Funcion para opciones del menu


#Ejecutar esa funcion
submenu.add_command(label="Salir", command=ventana.quit)
submenu.add_command(label="Saludar", command=mostrar_mensaje)

#Mostrar la ventana
ventana.mainloop()