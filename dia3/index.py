## con el metodo .index ("n") puedo buscar la posicion en la cual se encuentra la letra
mi_texto = "esta es una prueba "

resultado=mi_texto.index("n")

print (resultado)

## con este metodo puedo encontrar la palabra que se encuentra en la posicion numero 2 
mi_texto = "esta es una prueba "

resultado=mi_texto[2]

print (resultado)


## este busca la posicion de la letra de derecha a izquierda 
mi_texto = "esta es una prueba "

resultado=mi_texto.rindex("e")

print (resultado)


##Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"


palabra = "ordenador"


resultado = palabra[4]

print(resultado)


##Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:


frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado=frase.index("práctica")

print(resultado)   


##Práctica Método Index() 3 Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:


frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

resultado=frase.rindex("práctica")

print(resultado)     