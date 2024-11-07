#Diccionarios
diccionario = {} #diccionario vacio
# diccionario con 4 items
puertos = {
    22:'SSH',
    23:'Telnet',
    80:'HTTP',
    3306:'MySQL'
}
print(puertos)

#El metodo update agrega items de un diccionario en otro
puertos1 = {
    22:'SSH',
    80:'HTTP'
}
puertos2 = {
    53:'DNS',
    443:'HTTPS'
}
print(puertos1)
puertos1.update(puertos2)
print(puertos1)

#Comparar
#Se mira si los diccionarios tienen los mismos items
a = {123:'Rojas', 87:'Rosas'} == {87:'Rosas', 123:'Rojas', 78:'Otro'}
print(a)

#Accediendo al valor de un  item con la clave dada
puertos3 = {
22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}
protocolo = puertos3[22]
print(protocolo)
#puertos3[8080]#Error

#Eliminar item con la clave dada
calificaciones = {
    "alumnos1":5,
    "alumnos2":3,
    "alumnos3":4,
    "alumnos4":3
}
print(calificaciones)
del calificaciones ["alumnos3"]
print(calificaciones)

#Iterar un diccionario
#usar el ciclo for y el metodo items para obtener los items de un diccionario.
dicPuertos = {
    22:"SSH",
    23:"Telnet",
    80:"Http"
}
for x,y in dicPuertos.items():
    print(x, "->", y)