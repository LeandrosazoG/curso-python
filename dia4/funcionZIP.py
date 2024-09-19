nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Mexico','Madrid']

combinados = list(zip(nombres,edades,ciudades))

print(combinados)




#####


nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Mexico','Madrid']

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudades}")
    
    
    
####
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


combinado = list(zip(capitales,paises))

for capitales,paises in combinado:
    print(f'La capital de {paises } es {capitales}')