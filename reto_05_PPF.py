"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""
def primo(numero):
    resultado = ""
    if numero < 0:
        resultado = "no es primo"
    elif abs(numero % 2) == 1 or numero == 2:
        resultado = " es primo"
    else:
        resultado = "no es primo"
    return resultado

def fibonacci(numero):
    resultado = ""
    suma = 0 #Aca voy a almacenar el resultado, para ver si es fibo o no
    bandera = 0
    while bandera == 0:
        if suma == 0:
            suma += 1
        else:
            anterior_suma = suma   
            suma += anterior_suma
        if suma > numero:
            bandera = 1
            resultado = "no es fibo"
        elif suma == numero:
            bandera = 1
            resultado = "es fibo"  
    return resultado

    #Asi lo hace cgpt al fibo, me parece bueno tenerlo en cuenta.
    # def es_fibonacci(numero):
    # a, b = 0, 1
    # while b < numero:
    #     a, b = b, a + b

    # if b == numero:
    #     return "es fibo"
    # else:
    #     return "no es fibo"  

def par(numero):
    resultado = ""
    if numero % 2 : 
        resultado = "es impar" #Esto es true porque da 1, es impar
    else:
        resultado = "es par"
    return resultado

def condicion_numero(funcion1,funcion2,funcion3,numero): #Unicamente para ponerlo en practica HOF.
    return print(f'El numero {numero},{funcion1(numero)},{funcion2(numero)} y {funcion3(numero)}')

condicion_numero(primo,fibonacci,par,2)
condicion_numero(primo,fibonacci,par,7)

