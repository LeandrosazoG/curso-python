#creacion de diccionario y como buscar un valor en el mismo.

diccionario={'c1':'valor1','c2':'valor2'}

resultado=diccionario['c2']
print(resultado)



cliente={'nombre':'juan',
         'apellido':'fuentes',
         'peso':88,
         'talla':1.76}

consulta=cliente['peso']
print(consulta)


#dic  aqui puedo colocar dentro de un diccionario ,listas y buscar alguna dato especifico de esa lista
dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}



print(dic['c2'][1])

# aqui puedo buscar algun caracter dentro del 

abc={'c1':['a','b','c'],'c2':['d','e','f']}


print(abc['c2'][1].upper())


# aqui puedo agregar contenido a mi diccionario
diccionario2={1:'a',2:'b'}



diccionario2[3]='c'
#puedo tambien sobre escribir una posicion.
diccionario2[2]='B'

print(diccionario2)

#con el print keys me muestra en pantall los valores de la clave
print(diccionario2.keys())

# con el prin values nos muestra el valor que contiene la clave
print(diccionario2.values())

# este  me deja  ver todo los valores almacenados en el diccionario
print(diccionario2.items())



##Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print (mi_dict['puntos']['points2'][1]) 



#Actualiza la información de nuestro diccionario llamado mi_dic 
#(reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic['edad']=36
mi_dic['ocupacion']='Editora'
mi_dic['pais']='Colombia'


print(mi_dic)