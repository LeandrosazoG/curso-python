my_Set=set([1,2,3,4,5])


print(len(my_Set))

print(my_Set)


#con este codigo puedo ver si algun numero se encuentra en mi set 


my_Set=set([1,2,3,4,5])


print(2 in my_Set)


## union . puedo unir dos set 

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)

print(s3)


#con este metodo puedo agregar

s1={1,2,3}

s1.add(4)

print(s1)


# con este puedo elminar

s1={1,2,3}

s1.remove(2)

print(s1)


## discar es lo mismo que remove pero no se me cae si no ecuentra el numero para descargar
s1={1,2,3}

s1.discard(2)

print(s1)

# con este podemos eliminae todo lo que hay dentro de nuestro set
s1={1,2,3}

s1.clear()

print(s1)


# elimina un elemento al azar       
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.pop()

print(sorteo)