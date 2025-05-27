edad = int(27)
print(f"edad: (edad), Tipo: {type(edad)}")

altura = float(1.65)
print(f"Altura: {altura} Tipo: {type(altura)}")

z = 2+5j #complex
print(f"complejo: {z}. Tipo: {type(z)}")

cadena = "Juan"
print(f"nombre: {cadena}, Tipo{type(cadena)}")

verdadero = True
print(f"bool: {verdadero}, Tipo: {type(verdadero)}")

valor = None
infinito = float("inf")
print(f"Infinito: {infinito}, Tipo: {type(infinito)}")

Nan = float("nan")
print(f"Not a Number: {Nan}, Tipo: {type(Nan)}")

#Lista (arrays) -> Coleccion de elementos ordenados y cambiables
lista = ["algo", 17, 0.5, ["otra_lista", True]]
print(f"Lista: {lista},tipo: {type(lista)}")

#Tupla (tuple) -> CVoleccion de elementios ordenados inmutablesy que tiene una longitud fija(no se puede agregar ni eliminar)
tupla = (10.5, 48.5)

#Set -> Coleccioin de elementos unicos (no se pueden repetir), y no tienen un ordendefinido, sin embargosi son mutables (se puede agregar y eliminar elementos)
colores = {"azul", "rojo", "verde", "azul"}
print(colores)

#Diccionarios (Dic) -> es una coleccion de elementos que tienen pares clave-valor (key-value)
estudiante = {
    #clave : valor
    #key : value
    "nombre" : "Eduardo",
    "edad" : 17,
    "curso" : {
        "nombre" : "Programacion web",
        "iniciales" : ["PW", "WP"]
    }
}
print(estudiante)

#Busqueda de datos en diccionario
estudiante["curso"]["iniciales"][0] = "Python"
print(estudiante)
