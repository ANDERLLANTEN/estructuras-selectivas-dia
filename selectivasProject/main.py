# simple
a = 33
b = 200

if b > a:
    print(b, "es mayor que ",a)

#doble
y = 200
z = 333

if y > z:
    print(y, "es mayor que ",z)
else:
    print(y, "es mayor que ", z)

#multiple
q = 200
w  = 207
if q > w:
    print(q, "es mayor que ", w)
elif q < w:
    print(q, "es mayor que ", w)
else:
    print(q, "es mayor que ", w)


x = 28
if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")


print("estudiar los sabados ", end= '')
print("es genial")

print("estudiar los sabados ")
print("es genial")

print("daniela","luis","carlos","camila") #agregamos un espacio por defecto
print("daniela","luis","carlos","camila",sep="") #quita el espacio
print("daniela","luis","carlos","camila",sep=",") # aguega una coma

print("daniela","luis","carlos","camila", sep = "_", end= "_curso_python") #implementacion end y sed