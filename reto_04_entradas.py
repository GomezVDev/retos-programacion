import random #Me va a ayudar con los numeros y elecciones.
import string # Me va a ayudar con las letras y simbolos.

def creador_contrasenas_v2():
    bandera = 0
    eleccion_numeros, eleccion_mayus,eleccion_minus,eleccion_simbolos = 0,0,0,0
    while bandera == 0: #Para preguntar la configuracion de la contraseña
        total_eleccion = 0
        print("Este es un creador de contraseñas, donde minimo debe haber 8 digitos y maximo 16")
        eleccion_numeros =int(input("Cuantos numeros quieres poner? Mininimo 0 Maximo 16: "))
        total_eleccion += eleccion_numeros
        if total_eleccion < 16:
            eleccion_minus =int(input(f"Cuantas minusculas quieres poner? Mininimo 0 Maximo {16-total_eleccion}: "))
            total_eleccion += eleccion_minus
        if total_eleccion < 16:
            eleccion_mayus =int(input(f"Cuantas mayusculas quieres poner? Mininimo 0 Maximo {16-total_eleccion}: "))
            total_eleccion += eleccion_mayus
        if total_eleccion < 16:    
            if total_eleccion < 8:
                eleccion_simbolos =int(input(f"Cuantos simbolos quieres poner? Mininimo {8-total_eleccion} Maximo {16-total_eleccion}: "))
                total_eleccion += eleccion_simbolos
            else:
                eleccion_simbolos =int(input(f"Cuantos simbolos quieres poner? Mininimo 0 Maximo {16-total_eleccion}: "))
                total_eleccion += eleccion_simbolos
        if total_eleccion >=8 and total_eleccion <= 16: #Verifico que este dentro del rango
            bandera = 1
        elif total_eleccion <8:
            print("Ingresaste menos de 8 digitos, vuelva a indicar las cantidades")
        else:
            print("Ingresaste mas de 16 digitos, vuelva a indicar las cantidades")
            
    contrasena_creada = "" #Variable para la contraseña
    if eleccion_numeros > 0: #Voy agregando lo solicitado a la lista
        for x in range(eleccion_numeros): #Rango para los numeros
            contrasena_creada += str(random.randint(0,9)) #Para generar numeros del 0 al 9
    if eleccion_minus > 0: 
        for x in range(eleccion_minus):
            contrasena_creada += random.choice(string.ascii_lowercase) #Para generar abc 
    if eleccion_mayus > 0: 
        for x in range(eleccion_mayus):
            contrasena_creada += random.choice(string.ascii_uppercase) # Para generar ABC
    if eleccion_simbolos > 0: 
        for x in range(eleccion_simbolos):
            contrasena_creada += random.choice(string.punctuation) #Genero los simbolos.
    
    lista_contrasena_creada = list(contrasena_creada) #Esto para poder desordenarla.
    random.shuffle(lista_contrasena_creada) #La desordeno con shuffle.
    contrasena_creada_final = ''.join(lista_contrasena_creada) #Hago una nueva variable para guardar lo que retornare
    return contrasena_creada_final

contrasena1 = creador_contrasenas_v2()
print(f'{contrasena1} y {len(contrasena1)}')
        

