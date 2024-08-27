

lista1=[]
lista2=[]



cosa=input("ingresa algunos caracteres:").lower()
lista1.append(cosa)

letras=input("ingresa tres letras:").lower()
lista2.append(letras)

#aqui me muestra los el numero de caracteres que tiene la palabra que se ingresa

print("este es el largo de tu letras ingresadas ", len(cosa))
print("las palabras ingresadas en total son :",len(letras))
#MUESTRA LAS LISTAS ACTULIZADAS
print("esta es tu lista", lista1)
print("esta es tu lista de letras ", lista2)

#TEXO invertido
print(f"tu texto invertido seria a si : {cosa[: : -1]}")


#Texto invertido de letras
print(f"tu texto invertido de letras seria : {letras[: : -1]}")

#la palabra pyton se encuentra dentro del texto 

print("python " in lista1)


# la primera y ultima palabra 

if cosa :
    print(f"Primera letra de 'cosa': {cosa[0]}")
    print(f"Última letra de 'cosa': {cosa[-1]}")


if letras:
    print(f'primera letra de letras es : {letras[0]}')
    print(f'primera letra de letras es : {letras[-1]}')
    


