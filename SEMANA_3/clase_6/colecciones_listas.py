# Se definen con [] y pueden contener cualquier tipo de elemento, incluso otras lista o colccion
# Son ordenadas (sus elementos tienen indice) y son mutables(podemos eliminar, agregar o modificar)

       #  0  1  2  3  4
numero = [1, 2, 5, 8, 1, 4]

#primer elemento
print(numero[0])

#ultimo elemento
print(numero[-1])

# sublista (slicing)
print(f"Primeros 3 elementos: {numero[:3]}")
print(f"Ultimos 3 elementos: {numero[-3:]}")
print(f"Elementos del medio: {numero[1:-1]}")

print(f"Longitud de la lista: {len(numero)}")


print(f"### METODOS ###")


print(f"Cuantas veces aparece el elemento con valor 3: {numero.count(3)}")

print(f"Cual es el indice del elemtno con valor 3: {numero.index(5)}")

numero.append(6)
print(f"Lista luego del append(): {numero}")

numero[0] = 99
print(f"Despues de modificar: {numero}")

# Para el insert() primero le decimos en que posicion tiene que ir y despues elegimos el tipo de dato
numero.insert(0, 8)
print(f"Lista luego del insert: {numero}")

# El pop() se utiliza para eliminar un elemento de una lista designando que lugar, o en el caso de que no se le pase ningun valor te va a eliminar el ultimo
numero.pop()
print(f"Lista luego del pop: {numero}")

# El remove() te limina un elemento pero va por valor, no por indice(orden)
numero.remove(2)
print(f"Lista luego del remove: {numero}")

# Te ordena los numeros
numero.sort()
print(f"Lista luego del sort : {numero}")
numero.sort(reverse=True)
print(f"Lista luegos del sort reverse: {numero}")

# matriz es una lista llena de listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matriz: {matriz}")
print(f"Elemento [2][2]: {matriz[2][2]}")

#IMPORTANTE
print(f"Elemento con valor 5 esta en la lista?: {"SI" if 5 in numero else "NO"}")