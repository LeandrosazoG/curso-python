
# comparando tres numero
mi_boo = 4 < 5 < 6

print(mi_boo)


# and o (y) se tienen que cumplir las dos condiciones para que sea TRUE 

mi_bool= (4 < 5) and  (5 > 6 )

print(mi_bool)


#
tu_bool = (55 == 55) and ('perro'=='perro')

print(tu_bool)  


## en o si se cumple una condicion sera verdadero, para que sea false las dos deben ser falsa   

el_bool = 10 == 20 or 3==3

print(el_bool)

#busqueda de palabra


texto= "esta frase  es breve "
j_bool = 'frase ' in texto  and 'breve ' in texto
print(j_bool)


#not

l_bool= not 'a' == 'a'


print(l_bool)


#para saber lo contrario a lo que entrega la informacion

k_bool="esta frase es breve "

k_bool = not 'a ' != 'a'



##  enjercicio 

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool= not 'éxito' in frase and  not 'tecnología' in frase

print (mi_bool)