# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
recorte_1 = palabra_1[0:3]

# De la segunda palabra tome las primeras dos letras, utilice el operador :
recorte_2 = palabra_2[0:2]

# Formar una nueva palabra con los recortes solicitados
nueva_palabra = recorte_1 + recorte_2

# Imprima en pantalla los resultados
print('la primer palabra es:',palabra_1)
print('la segunda palabra es:', palabra_2)
print('los recortes son:', recorte_1, 'y', recorte_2)
print('la nueva palabra es:', nueva_palabra)