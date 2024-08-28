
letras=[]

texto=input("ingresa algunos caracteres:").lower()

texto =texto.lower()

letras.append(input("ingresa tres letras:").lower())
letras.append(input("ingresa segunda letras:").lower())
letras.append(input("ingresa tercera letras:").lower())



#aqui me muestra los el numero de caracteres que tiene la palabra que se ingresa
print("Las palabras ingresadas en total son:", len(texto.split()))
print("las palabras ingresadas en total son :",len(letras))


#TEXO invertido
print(f"tu texto invertido seria a si : {texto[: : -1]}")


#Texto invertido de letras
print(f"tu texto invertido de letras seria : {letras[: : -1]}")

#la palabra pyton se encuentra dentro del texto 

print("python " in texto)


# la primera y ultima palabra 

if texto :
    print(f"Primera letra de tu texto es : {texto[0]}")
    print(f"Última letra de de tu texto es : {texto[-1]}")


if letras:
    print(f'primera letra de letras es : {letras[0]}')
    print(f'primera letra de letras es : {letras[-1]}')
    


