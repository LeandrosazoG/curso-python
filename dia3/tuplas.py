#puedo buscar la posicion de algun numero

mi_tuple=1,2,3,4


print(mi_tuple[0])


#puedo crear tuplas dentro de tuplas (anidar)

mi_tuple=1,2,(10,20),4

# aqui puedo buscar una tupla dentro de otra y buscar el valor que necesito.
print(mi_tuple[2][0])



t=(1,2,3)

x,y,z=t

print(x,y,z)

##Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista=list(mi_tupla)
print(mi_lista)


##con lent puedo ver el largo de mi lista
t=(1,2,3,)

x,y,z=t

print(len(t))



#con wl metodo count puedo hacer que me cuente cuantas veces aparece un caracter en la tupla
t=(1,2,3,1)



print(t.count(1))



##puedo encontrar el valor de indice 
t=(1,2,3,1)



print(t.index(2))




