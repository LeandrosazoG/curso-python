## CREANDO MENU
print("BIENVENIDO AL BANCO LEANDRO \n")

saldo=50000

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
        print(f"tu saldo contable es de : {saldo}")
        break
    elif opciones == 2:
        print("ENTRASTE A TU CUENTA CORRIENTE CORRECTAMENTE")
        break
    elif opciones == 3: 
        saldo_retiro=int(input("ingresa cuando es el monto que deseas retirar :"))
        saldo_final= saldo-saldo_retiro
        print(f"TU ESTADO DE CUENTA SON :{saldo_final}")
        print("TU DINERO SERA RETIRADO EN BREVE")
        break
    elif opciones == 4:
        print("tus pagos se recivieron correctamente ")
        break
    elif opciones == 5:
        print ("tu comprobante sera imprimido en breve ")
        break
        
    else:
        print("INGRESA UNA OPCION VALIDA !!!")



