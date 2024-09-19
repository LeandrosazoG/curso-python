while True : 
    n = int(input("cuantas edades vas ingresas (n) :"))
    if n > 0 :
        break
    else :
        print("debes ingresar un numero mayor > 0 ")
        
        
suma = 0 # la suma parte de cero 
edad_mayor=-1 # se asuma que la edad mayor esta fuera del rango posible 
edad_menor = 100 # se asume que la edad menor esta guera del rango posible 


for i in range (n): # 4 edades : 18 - 45  71 - 22
    while True : 
        edad=int(input("ingrese edad "))
        if edad > 0:
            break
        else :
            print("debes ingresar una edad  >=0 ")
        ## para que funcione el if ( este siempre debe esta fuera del ultimo else )
    if edad >edad_mayor:
            edad_mayor=edad
    if edad < edad_menor:
            edad_menor=edad
        
    suma+=edad
    
promedio = int(suma/n)

print(f"el promedio de edad es {promedio}")
print(f"La edad mayor  es : {edad_mayor}")
print(f"la edad menor es : {edad_menor}")