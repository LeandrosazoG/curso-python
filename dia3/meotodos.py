
#tranformar el texto en mayuscula .upper()

texto="este es el texto de federico "

resultado=texto.upper()
print(resultado)



## transforma el texto en minuscula
texto="ESTE TEXTO ES DE FEDERICO "

resultado=texto.lower()
print(resultado)


## aqui se puede guardar el texto en una lista. 
texto="ESTE TEXTO ES DE FEDERICO "

resultado=texto.split("T")
print(resultado)


## aqui  guardamos el texto en una lista  y sacamos las palabras que esten junto a la t
texto="ESTE TEXTO ES DE FEDERICO "

resultado=texto.split("T")
print(resultado)



## con este metodo puedo unir las variables  a travez de una lista

a="aprender"
b="python"
c="es"
d="genial"
e=" ".join([a,b,c,d])


print(e)

#buscamos un caracter de nuestro str    

texto="ESTE TEXTO ES DE FEDERICO "

resultado=texto.find("S")
print(resultado)

#con replace puedo cabambiar el texto. el primero es el texto que deseo cambiar y el segundo el que deseo agregar por ese   

texto="ESTE TEXTO ES DE FEDERICO "

resultado=texto.replace("FEDERICO,TODOS")
print(resultado)


#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.


lista_palabras = ["La","legibilidad","cuenta."]

resultado=" ".join(lista_palabras)


print(resultado)


## aqui puedo remplazar mas de dos palabras.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

resultado= frase.replace("difícil","fácil").replace("mala","buena")

print(resultado)
