print( "porfavor prende la luz on y apagar luz off ")

luz = input("ingresa encendido o apagado de luz ").lower()


while True:
    if luz == 'on':
        print ("haz prendido la luz ")
    elif luz == 'off':
        print('haz apado la luz correctamente')
    else:
        print("elige una de las dos opciones Porfavor !!!")
        break
    
    
