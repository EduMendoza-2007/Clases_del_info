"""Este es un modulo"""
# import random

# def generar_hechizos():
#     prefijos = ["Abra", "Alakaza", "Zendo", "Foco", "Magi"]
#     sufijos = ["cadabra", "lumos", "mora", "nox", "flama"]
#     prefijo_aleatorio = random.choice(prefijos)
#     sufijo_aleatorio = random.choice(sufijos)
#     hechizo = f"{prefijo_aleatorio}-{sufijo_aleatorio}"
#     return hechizo

# print(generar_hechizos())

estudiantes = {
    'Ana': [9, 8, 10],
    'Luis': [4, 6, 5],
    'Carlos': [10, 10, 9]
}

def agregar_estudiante(nombre, notas, base):
    base[nombre] = notas

agregar_estudiante("Edu", [10, 10, 10], estudiantes)

def promedio_estudiante(base, nombre):
    notas = base[nombre]
    #El get hae que no nos de error cuando traigamos un alumno que no este en el diccionario
    return sum(notas) / len(notas)

print(f"El promedio del estudiante 'Luis' es: {promedio_estudiante(estudiantes, "Luis")}")

def estudiantes_aprobados(base, nombre):
    aprovados = []
    desaprovados = []
    if promedio_estudiante(base, nombre) >=8:
        return f"Weeeee paraaaa {nombre}, maquina del mal", aprovados.append(nombre)
    elif promedio_estudiante(base, nombre) >= 6:
        return f"Safaste {nombre}, estudiante mucho", aprovados.append(nombre)
    else:
        return f"Te veo en marzo {nombre}, segui estudiando", desaprovados.append(nombre)

print(estudiantes_aprobados(estudiantes, "Luis"))
