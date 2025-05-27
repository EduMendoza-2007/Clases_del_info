
saludo = "Hola"
sujeto = "info"

print(saludo + " " + sujeto)

num1= 10
num2 = 5

print(num1 + num2)

Intento = "estoy haciendo lo posible"

mensaje = f"Estoy practicando, {Intento}"
print(mensaje)

cadena_1 = "hola"
cadena_2 = "mundo"
concatenacion = cadena_1 + " " + cadena_2
print(concatenacion)
        # 12345678910
cadena = "holA mundo"
longitud = len(cadena)
print(longitud)

subcadena = cadena[0:4]
print(subcadena)

cadena_invertida = cadena[::-1]
print(cadena_invertida)

cadena_mayuscula = cadena.upper()
print(cadena_mayuscula)

cadena_minuscula = cadena_mayuscula.lower()
print(cadena_minuscula)

cadena_capitalize = cadena_minuscula.capitalize()
print(cadena_capitalize)

cadena_remplazo = cadena.replace("hola", "algo")
print(cadena_remplazo)

print("hola\nmundo")
print("hola\tmundo")
print("hola\\mundo")
print("hola \"mundo\"")
print("hola", end="!")
print("mundo")
print("hola", "mundo", "info", sep="\t")