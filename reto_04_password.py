"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

#Voy a empezar importando librerias que me van a ayudar a generar lo que necesito.
import random #Me va a ayudar con los numeros y elecciones.
import string # Me va a ayudar con las letras y simbolos.

def creador_contrasenas(): #No necesita ningun parametro
    contrasena_generada = ''#Para guarda la cc.

    for x in range(random.randint(8,17)): #Aca un for de 8 a 16 "digitos"
        numero_aleatorio = random.randint(1,4) #Para elegir una de las 4 opciones
        if numero_aleatorio == 1:
            numero_aleatorio_contrasena = random.randint(0,9) #Ya que necesito numeros del 0 al 9
            contrasena_generada += str(numero_aleatorio_contrasena)
        elif numero_aleatorio == 2:
            letra_aleatoria_minuscula = random.choice(string.ascii_lowercase) #El .choise me ayuda a elegir entre las opciones que le pongo, en este caso las minusculas
            contrasena_generada += letra_aleatoria_minuscula
        elif numero_aleatorio == 3:
            letra_aleatoria_mayuscula = random.choice('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ') #Un mejor ejemplo del random.choice
            contrasena_generada += letra_aleatoria_mayuscula
        else: 
            simbolo_aleatorio = random.choice(string.punctuation) #punctuation son los simbolos
            contrasena_generada += simbolo_aleatorio
    return contrasena_generada  #Devuelve la contraseña

contrasena1 = creador_contrasenas()
print(f'{contrasena1} y la longitud es {len(contrasena1)}')

contrasena2 = creador_contrasenas()
print(f'{contrasena2} y la longitud es {len(contrasena2)}')

contrasena3 = creador_contrasenas()
print(f'{contrasena3} y la longitud es {len(contrasena3)}')


