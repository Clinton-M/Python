# listas


# lista = ["manzanas", "peras", "uvas", "naranjas", "limones"]

# print(lista)

# lista.insert(0, "sandia")

# lista.append("fresa")

# print(lista)

# lista.remove("manzanas")
# print(lista)

# for i in lista:
#     print(i)

# for index, i in enumerate(lista):
#     print(index, i)


# #diccionarios

diccionario1 = {"nombre": "juan", "apellido": "perez", "edad": "25"}
diccionario2 = {"nombre": "clinton", "apellido": "mejia", "edad": "21"}

anidado = {"diccionario1": diccionario1, "diccionario2": diccionario2}


diccionario1.get("nombre")

# print("el valor de la clave nombre es: " + diccionario2.get("nombre"))

#set o conjunto

conjuto = ["manzanas", "peras", "uvas", "naranjas", "limones", "limones", "uvas"]

#pasar a ser el conjunto
set(conjuto)
print(set(conjuto))

print(len(set(conjuto)))
#ubicar un valor en un conjunto
print("peras"in set(conjuto))



conjuntoo = set([1,1,1,2,2,23,5,4])

print(conjuntoo)