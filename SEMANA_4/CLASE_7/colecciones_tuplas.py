# Se definen con parentesis () y pueden contener cualquier tipo de elemento, incluso otras listas, o coleccioines.
# Son ordenadas (sus elementos tienen indice) y son inmutables(no se pueden modificar)

numeros_tupla = (1, 2, 3, 4, 5)

#Primer elemento
print(numeros_tupla[0])

#ultimo elemento
print(numeros_tupla[-1])


# Longitud
print(f"longitud de la tupla: {len(numeros_tupla)}")

#No se puede modificarlos
#numeros[0] = 0

#Desempaquetado de tupla
a, b, c, d, e= numeros_tupla
print(f"Desempaquetando: a={a} b={b} c={c} d={d} e={e}")

primer_elemento, *resto_de_elementos = numeros_tupla
print(f"Desempaquetado: Primero={primer_elemento},Resto{resto_de_elementos}")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz: {matriz}")
print(f"Elemento [2][2]: {matriz[1][1]}")

persona = ("Juan", 23, 1.85, True)
print(f"Persona: {persona}")

print(f"Elemento con valor 'Juan' esta en la tupla?: {"si" if "Juan" in persona else "no"}")

lisa_numeros = list(numeros_tupla)
print(f"Tupla convertida a lista: {lisa_numeros}")

lisa_numeros.append(88)
print(f"Lista luego del append: {lisa_numeros}")
tupla_numeros = tuple(lisa_numeros)
print(f"Lista pasada a tupla: {tupla_numeros}")