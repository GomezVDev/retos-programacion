"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

for n in range(1,101):            #Hago un ciclo para que me muestre 100 numeros.
    if n % 3 == 0 and n % 5 == 0: #Muestro los que sean multiplo a la vez
        print("fizzbuzz")
    elif n % 3 == 0:              #Luego los que son solo multiplos de 3
        print("fizz")
    elif n % 5 == 0:              #Multiplos de 5
        print("buzz")
    else:                         # No son multiplos de lo pedido.
        print(n)



