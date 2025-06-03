# def saludo(nombre):
#     print(f"Hola {nombre}")

# saludo("Pablo") 
# saludo("Elias")
# saludo("Edu")

# notas = [10, 5, 7, 8]
# suma = 0

# for nota in notas:
#     suma += nota

# print(suma)

# promedio = suma / len(notas)

# print(f"Suma: {suma}")
# print(f"Cantidad de notas: {len(notas)}")
# print(f"Promedio: {promedio}")

# def promedio(notas):
#     return sum(notas) / len(notas)

# promedio_Edu = promedio([5, 6, 8, 9])
# promedio_Juan = promedio([])

# print(promedio_Edu)
# print(promedio_Juan)

# estudiantes = [
# {
# "nombre": "Juan",
# "notas": {
# "mate": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# },
# "castellano": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# },
# "ingles": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# }
# }
# },
# {
# "nombre": "Pablo",
# "notas": {
# "mate": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# },
# "castellano": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# },
# "ingles": {
# "trimestre_uno": 10,
# "trimestre_dos": 5,
# "trimestre_tres": 8,
# }
# }
# }
# ]

# variable_global = "global"

# def prueba():
#     variable_local = "local"
#     print(variable_local)

# prueba()
# print(

#*args: Permiten pasar a una funcion un numero variable/ indeterminado de argumentos posicionales...

#ALta calculadora hermano

# def suma(*numeros):
#     """Calculadora solamente para suma"""
#     print(numeros)
#     print(type(numeros))

#     resultado = 0
#     for numero in numeros:
#         resultado += numero

#     return resultado

# resultado = suma(10, 10, 10, 20, 30)
# print(f"Resultado es: {resultado})


#*kwargs:Permiten pasar a una funcion un numero de variables/ indeterminado de argumentos con nombre(clave)-valor)


# def ver_persona(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     for clave, valor in kwargs.items():
#         print(f"Clave: {clave}, Valor: {valor}")

# ver_persona(nombre = "Juan", edad = 25, ciudad = "Resistencia")

#Respetar el orden siempre
         #indeterminados o determinados
                 #posicionales
def mostrar_info(*args, nombre, edad=0, **kwargs):
                                    #nombrados
                         #determinados o indeterminados
    print(f"Posicionales indeterminados {args}")
    print(f"Nombrados indeterminados: {kwargs}")
    print(f"posicionales determinados: {nombre}")
    print(f"Nombrados determinados: {edad}")

mostrar_info(50, True, "algo", nombre="Pablo", edad=20, ciudad="Resistencia")