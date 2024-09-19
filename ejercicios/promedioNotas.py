while True :    ## validacion de  que ingrese una mas notas 
    n=int(input("ingresa el numero de notas "))
    if n > 0 :
        break
    else : 
        print("ingrese al menos dos notas o mas ")
        
suma = 0
nota_mayor=-1 
nota_menor = 200
# Bucle para ingresar las notas y calcular los valores requeridos
for i in range (n):
    while True:
        nota = int(input("ingrese sus notas :"))
        if nota > 0 : 
            break
        else:
            print("Debes ingresar nota >=0")
        
    if nota > nota_mayor:
        nota_mayor = nota
    if nota < nota_menor:
         nota_menor = nota
        
    suma+=nota # suma de las notas 
promedio = int(suma/n) # calcular promedio
    
print(f"el promedio de edad es {promedio}")
print(f"La nota  mayor  es : {nota_mayor}")
print(f"la nota  menor es : {nota_menor}")
    
    