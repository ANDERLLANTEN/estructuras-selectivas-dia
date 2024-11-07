# tuplas
tupla1 = () # definir una tubla vacia
print(tupla1)

tupla2 = ("una cadenas",123,4.9,True) # una tupla heterogenea
print(tupla2)
print(tupla2[1]) # acceder al elemento de la tubla
print(tupla2[3])

#enlazar tuplas
tupla3 = (0,1,2,3)
tupla4 = ("A",  "B", "C")
tupla5 = (tupla3,tupla4)
print(tupla5)
print(tupla5[1][1]) # muestra de la tupla2 el elemento en el indice 1
print(tupla5[1][0])
print(tupla5[0][3])

#operaciones con las tuplas
tupla6 = ("A",  "B", "C", "D", "E")
tupla7 = (1,2,3,4,5,)
tupla8 =tupla6 + tupla7 # concatenar
print(tupla8)
print(tupla8[8])

#repetir una tupla
tupla9 = (1,2,3,4,5)
tupla10 = tupla9 * 3
print(tupla10)

#comparar una tupla
tupla11 = ("Rojas")
tupla12 = (123)
tupla13 = ("Rosas")
tupla14 = ("rosas")
print((tupla11,tupla12) < (tupla13, tupla14))

print((tupla13,tupla14) == (tupla11,tupla12))

