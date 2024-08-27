texto =     "ABCDEFGHIJKLM"

#aqui puedo buscar los caracteres que van desde el 2, hasta el 5, pero no incluyendolo
fracmento = texto[2:5]

print(fracmento)



texto =     "ABCDEFGHIJKLM"

#aqui puedo buscar los caracteres que van desde 2 hasta el final.
fracmento = texto[2:]

print(fracmento)




texto =     "ABCDEFGHIJKLM"

#con el ultimo caracter puedo ir saltandome lineas cada 2
fracmento = texto[::2]

print(fracmento)



texto =     "ABCDEFGHIJKLM"

#orden inverso
fracmento = texto[::-1]

print(fracmento)



#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
frase = "Controlar la complejidad es la esencia de la programación"

fracmento = frase[0:9]

print(fracmento)


##Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

fragmento=frase[8::3]

print(fragmento)



##Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"


fragmento= frase[::-1]  