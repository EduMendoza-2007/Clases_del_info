# Se definen con llaves {} y pueden contener cualquier tipo de elento, sin embargo no los unhashable(solo tuplas)
# Son deordenadas (sus elementos no tienen indice) y son mutables(agregar, eliminar o modificar), sin embargo, no pueden conmtener elementos duplicados

colores = {"rojo", "azul", "verde"}
print(f"Conjunto set: {colores}, {type(colores)}")

#no se pueden acceder con indices porque son desordenadas

colores.add("amarillo")
print(f"Set luego del add: {colores}")
colores.add("amarillo")
print(f"Set luego del add: {colores}")

colores.remove("verde")
print(f"Set despues del remove: {colores}")

colores.discard("verde")
print(f"Set despues del discard: {colores}")

elemento_eliminado = colores.pop()
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Set lluego del pop: {colores}")

colores.clear()
print(f"Set luego del clear: {colores}")

colores = {"rojo", "azul", "verde"}
print(f"El color 'rojo' esrta en el set: {"rojo" in colores}")

conj1 = {1, 2, 3}
conj2 = {4, 5, 6}

union_conj = conj1.union(conj2)
print(f"Union: {union_conj}")

interseccion_conj = conj1.intersection(conj2)
print(f"Interseccion: {interseccion_conj}")

diferencia_conj = conj1.difference(conj2)
print(f"Diferencia: {diferencia_conj}")

listas_con_duplicados = [1, 1, 2, 3, 3, 4, 5, 6]
listas_sin_duplicados = list(set(listas_con_duplicados))

print(f"Lista sin duplicados: {listas_sin_duplicados}")