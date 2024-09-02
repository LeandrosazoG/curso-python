nombres=['juan','ana','carlos','belen','fran']

for elemento in nombres:
    print("hola" + "  " +elemento)
    

lista=["a","b","c"]

for letra in lista:
    print("Letra"+" " +letra)
    
    
#### aqui puedo hacer un ciclo ford agregando numero a cada letrwa 

lista=[1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"letra {numero_letra} :{letra}")
    
## con starswith puedo encontrar los nombres que comienzan en su primera palabra l
lista =["pablo","laura","luis","julia"]  

for nombre in lista :
    if nombre.startswith('l'):
        print(nombre)
    
 ### convinacion con loops   
    
lista =["pablo","laura","luis","julia"]

for nombre in lista :
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("nombre que comienza con l")
        
        
        
        
        
numeros=[1,2,3,4,5]

mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
    
    
    
    #### aqui te escribe la palabra en tipo cascada hacia abajo letra por letra 
    
palabra = 'python'

for letra in palabra :
    print(letra)
    
    
    
####puedo iterar una lista de otra lista cargando a= el primer valor y a b el segundo valor 
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    

####

dic  = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.items():
    print(item)
    
   #### 
dic  = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.values():
    print(item)



###
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0 
for num in lista_numeros:
    suma_numeros+=num
    print("la suma de numero es ",suma_numeros)




##### ejercicios sumar los pares y impares 
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:  # Si el número es par
        suma_pares += num #aqui sumo
    elif num % 2 == 1:  # Si el número es impar
        suma_impares += num

print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)


## a si se busca un numero par 
listas_n = [1,3,6,8]

for num in listas_n:
    if num % 2 == 0:
        print("estos son los numeros pares",num)
        
### a si se busca un inpar


listas_n = [1,3,6,8]

for num in listas_n:
    if num % 2 == 1:
        print("estos son los numeros inpares ",num)
        