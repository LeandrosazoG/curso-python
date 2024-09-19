lista = ['a','b','c']
indice = 0 

for item in lista:
    print(indice,item)
    indice+=1 
    
    
  ###
  
lista = ['a','b','c']


for item in enumerate(lista):
    print(item)
 

###
lista = ['a','b','c']


for item in enumerate(range(50,55)):
    print(item)
 

##
lista = ['a','b','c']

mis_tuples=list(enumerate(lista))
print(mis_tuples[1][0])




#### ejericio 

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
indice=0

for indice, nombre in enumerate(lista_nombres):
  print(f'{nombre} se encuentra en el índice {indice}')
  
  
###
cadena = "Python"
lista_indices = list(enumerate(cadena))

print(lista_indices)



####

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
