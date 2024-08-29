## CREANDO MENU
print("BIENVENIDO AL BANCO LEANDRO \n")


contraseña_correcta=123

while True:
    contraseña=int(input("ingrese su contraseña:"))
    if contraseña == contraseña_correcta:
        print("haz ingresado correctamente\n")
        print("opcion 1: revisar estado de cuenta\n")
        print("opcion 2: entrar en mi cuenta corriente\n")
        print("opcion 3 : retirar dinero en efectivo\n")
        print("opcion 4 : pago de servicios\n")
        print("opcion 5 : imprimir comprovante\n")
        break
    else:
        print("!!!!vuelva a ingresar contraseña correcta!!!")
        
while True:
    opciones=int(input("ingrese una opcion "))
    if opciones == 1:
        print("TU ESTADO DE CUENTA SON $50000 ")
    elif opciones == 2:
        print("ENTRASTE A TU CUENTA CORRIENTE CORRECTAMENTE")
    elif opciones == 3: 
        print("TU DINERO SERA RETIRADO EN BREVE")
    elif opciones == 4:
        print("tus pagos se recivieron correctamente ")
    elif opciones == 5:
        print ("tu comprobante sera imprimido en breve ")
        break
        
    else:
        print("INGRESA UNA OPCION VALIDA !!!")



