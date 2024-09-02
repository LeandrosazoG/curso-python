### el primero es desde donde, el segundo es hasta donde, y el 3 ero es para saltarse cada ciertos nuermos 

for numero in range (1,5):
    print(numero)
    
    
    
######
lista = list(range(1,101))
print(lista)
    


####Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(3,301,3)) 


###
suma_cuadrados = 0  # Inicializa la variable para acumular la suma

for numero in range(1, 16):  # Crea un rango del 1 al 15 (inclusive)
    suma_cuadrados += numero ** 2  # Calcula el cuadrado y lo suma a suma_cuadrados

print(suma_cuadrados)  # Muestra el resultado final