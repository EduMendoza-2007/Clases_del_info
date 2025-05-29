contador = 0


#     while True:
#         contador += 1
#         print("Hola hace frio {contador} veces")
# Ctrl + C para frenar el bucle

# flag = True
# while flag:
#     print("Hola info")
#     respuesta = input("Desea continuar? s/n: ")

#     if respuesta == "n":
#         flag = False

# flag = True
# while True:
#     print("Hola info")
#     respuesta = input("Desea continuar? s/n: ")

#     if respuesta == "n":
#         break

while True:
    print("Hola info")
    respuesta = input("Desea continuar? s/n: ")

    if not respuesta == "s" and respuesta == "n":
        print("Introduce una respuesta valida")
        continue

    if respuesta == "n":
        break