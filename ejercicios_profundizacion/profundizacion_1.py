# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('a continuación te solicitaré dos números y luego haremos distintas operaciones matemáticas con ellos')
print('ingresa el primer número')
primer_numero = float(input())
print('ingresa el segundo número')
segundo_numero = float(input())
resultado_suma = primer_numero + segundo_numero
resultado_resta = primer_numero - segundo_numero
resultado_multiplicacion = primer_numero * segundo_numero
resultado_division = primer_numero / segundo_numero
resultado_potencia = primer_numero ** segundo_numero
print('____')
print(' ')
print('el resultado de sumar', primer_numero, 'con', segundo_numero, 'es', resultado_suma)
print('el resultado de restar', primer_numero, 'con', segundo_numero, 'es', resultado_resta)
print('el resultado de multiplicar', primer_numero, 'con', segundo_numero, 'es', resultado_multiplicacion)
print('el resultado de dividir', primer_numero, 'con', segundo_numero, 'es', resultado_division)
print('la potencia que tiene como base a', primer_numero, 'y como exponente a', segundo_numero, 'da como resultado', resultado_potencia)
print(' ')
print(' ')
