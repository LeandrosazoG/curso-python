##num1 = int(input("Ingresa un número:"))
##num2 = int(input("Ingresa otro número:"))


##if num1 > num2:
   ## print("el num1 es mayor")
    
##elif num2 > num1:
      ##  print("el num2 es mayor")
        
##else :
        ##print ("son iguales ")
        
        
        
##
edad = 16
tiene_licencia = False

if edad > 18:
    print("Puedes conducir")

if edad < 18 :
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

elif tiene_licencia ==False:
    print("No puedes conducir. Necesitas contar con una licencia")



##


habla_ingles = True
sabe_python = False

# Evaluar las condiciones y mostrar el mensaje correspondiente
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
    
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    
elif not habla_ingles:
    
    print("Para postularte, necesitas tener conocimientos de inglés")
    
elif not sabe_python:
    print("Para postularte, necesitas saber programar en Python")