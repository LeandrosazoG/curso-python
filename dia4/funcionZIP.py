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




##### 
# Listas de números en diferentes idiomas
espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

# Creando el objeto zip y convirtiéndolo en una lista
numeros = list(zip(espanol, portugues, ingles))
