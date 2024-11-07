
#definicion de una lista
lista = [] #lista vacia
lista1 = ['Este es un texto'] #Una lista con un elemento
lista2 = ['Una cadena', 123] #Una lista de dos elementos
lista3 = [1, 2, 3, 4.5, 'hola', 'a'] #Una lista de seis elementos
print(lista)
print(lista1)
print(lista2)
print(lista3)

lista4 = [0, 1, 2, 3]
lista5 = ['A', 'B', 'C']
lista6 = [lista4, lista5]
print(lista6)
print(lista6[0]) #muestra lista4
print(lista6[1]) #muestra lista5
print(lista6[1][0]) #muestra de la lista5 el elemento del indice 0

#concatenacion
lista7 = ['A', 'B', 'C', 'E']
lista8 = [1, 2, 3, 4, 5]
lista9 = lista7 + lista8
print(lista9)
print(lista9[2])

#el metodo extend agrega una lista al final de otra lista, la operacion afecta la lista invocante
nombres1 = ['Antonio', 'Maria', 'Mabel']
nombres2 = ['Barry', 'John', 'Guttag']
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#repetir
lista10 = [1, 2, 3, 4, 5]
lista11 = lista10*3
print(lista11)

#comparacion
#usando los operadores convencionales(<, <=, >, >=, ==, !=)
print(['Rojas', 123] < ['Rosas', 123])
print(['Rosas', 123] == ['rosas', 123])
print(['Rosas', 123] > ['Rosas', 23])

#Es posible determinar si un elemento se encunetra en una lista
lista12 = ['cien', 'años', 'de', 'soledad']
if 'de' in lista12:
    print('Si esta en la lista')
else:
    print('No esta en la lista')

#Iterando una lista
lista13 = ['hola', 'amigos', 'mios']
for palabra in lista13: #para cada palabra de la lista
    print(palabra, end=',') # end evita salto de linea