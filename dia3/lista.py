# aqui puedo ver el largo de mi lista
mi_lista=['a','b','c']

resultado=len(mi_lista)


print(resultado)


# aqui puedo ver el primer caracter de mi lista que esta en la posicion 0 

mi_lista=['a','b','c']

resultado=mi_lista[0]


print(resultado)

#aqui puedo ver  desde que elemento necesito ver hasta el otro elemento sin incluirlo 
mi_lista=['a','b','c']

resultado=mi_lista[0:2]


print(resultado)

#aqui puedo concantenar dos listas 
mi_lista=['a','b','c']
mi_lista2=['d','e','f']

print(mi_lista +mi_lista2)

# en esta parte puedo modificiar la letras indicando su posicion y indicando la palabras que lo sustituira

mi_lista=['a','b','c']
mi_lista2=['d','e','f']
mi_lista3=mi_lista+mi_lista2

mi_lista3[0] = 'alfa'



print(mi_lista3)


# con el metodo append puedo agregar mas cosas a mi lista. 

mi_lista=['a','b','c']
mi_lista2=['d','e','f']
mi_lista3=mi_lista+mi_lista2

mi_lista3.append('g')
mi_lista3.append('h')



print(mi_lista3)


# con el meotodo pop interpreta que deseas elimiar el ultimo elemento a no se que tu especifiques cual deseas eliminar 
mi_lista=['a','b','c']
mi_lista2=['d','e','f']
mi_lista3=mi_lista+mi_lista2

mi_lista3.pop(0)



print(mi_lista3)


## es un metodo ordena la lista 

lista=['g','o','b','m','c']

lista.sort()

print(lista)



##Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

eliminado=frutas.pop(2)

print(frutas)
print(eliminado)