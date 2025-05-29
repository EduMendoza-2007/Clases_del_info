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

def promedio(notas):
    return sum(notas) / len(notas)

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

variable_global = "global"

def prueba():
    variable_local = "local"
    print(variable_local)

prueba()
print(variable_global)
