
#con esto puedo multiplicar mi str en el print por las veces que yo coloque 

n1= "Kari"
n2="na"
print(n1*10)

#con las tres comillas simples puedo generar saltos de lineas sin la necesidad de /n

poema="""mil pequeños peces blancos 
como si hiviera 
el color del agua """

print(poema)


# aqui podemos buscar si en nuestro poema se encuentra la palabra agua, si esta no retonara TRUEE y si no esta la palabra false 
poema="""mil pequeños peces blancos 
como si hiviera 
el color del agua """

print("agua" in poema)

# lo mismo pero negando que la palabra se encuentra en nuestro poema 
poema="""mil pequeños peces blancos 
como si hiviera 
el color del agua """

print("agua" not in poema)


#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
poema="""Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in poema)


#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

n="electroencefalografista"

print(len(n))


# con len podemos ver cuantos caracteres tiene el poema 
poema="""mil pequeños peces blancos 
como si hiviera 
el color del agua """

print(len(poema))