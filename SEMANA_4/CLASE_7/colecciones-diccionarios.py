#se definen con llaves {} y pestan conmpuestos por pares (clave-valor  key-value)
#Las llaves son unicas, y los valores pueden ser cualquier tiopois de datos incluso otros diccionarios
#Son desordenados (sus elementos no tienen indice) y son mutables(podemos agregar, eliminar)

estudiante = {
    "nombre": "Ana",
    "edad": 23,
    "curso": "Matematicas",
    "cabello": {
        "color":"rubio"
    }
}
print(f"Conjunto diccionario: {estudiante}, {type(estudiante)}")

print(f"Edad estudiante: {estudiante['edad']}")

estudiante["carrera"] = "ing"
print(f"Estudiante: {estudiante}")

del estudiante["carrera"]
print(f"Estudiante: {estudiante}")

print(f"Claves de diccionario: {list(estudiante.keys())}")

print(f"Valores del diccionario:{list(estudiante.values())}")

estudiante_dos = {
    "nombre": "Juan",
    "edad": 23,
    "curso": {
        "nombre": "Programacion web",
        "tags": ["PW", "Programacion", "web", "Python"]
    }
}
print(f"Estudiante dos: {estudiante_dos['curso']['nombre']}")
calificaciones = {
    "quimica": 10,
    "fisica": 5,
    "lengua": 7
}
for materia, nota in calificaciones.items():
    print(materia, nota)