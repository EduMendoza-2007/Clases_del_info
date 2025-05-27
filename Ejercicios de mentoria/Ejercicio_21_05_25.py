lista_compras = []

lista_compras.append("manzana")
lista_compras.append("naranja")
lista_compras.append("pera")

print("Esta es su lista de compras",lista_compras)

print(len(lista_compras))

lista_compras.pop(2)

print(lista_compras)

colores = ["rojo", "azul","verde","rojo","azul","verde"]

cantidad_rojo = colores.count("rojo")

print(cantidad_rojo)

indice_primer_verde = colores.index("verde")
print(indice_primer_verde)