'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 '''
#Voy a hacer una version simple, sin mucha comprobración de entradas.

def convertidor_hacker(texto):
        
        leet_dict = { #Hago un dict, para hacer sencillo el acceso a cada modificacion.
        'A': '4',
        'B': 'I3',
        'C': '[',
        'D': ')',
        'E': '3',
        'F': '|=',
        'G': '&',
        'H': '#',
        'I': '1',
        'J': ',_|',
        'K': '>|',
        'L': '|_', #Tambien es 1, no quiero repetir.
        'M': "|\/|",#Esta mejor
        'N': '^/',
        'O': '0',
        'P': '|*',
        'Q': '(_,)',
        'R': '|2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': '\/',
        'W': '\/\/',
        'X': '><',
        'Y': '`/', #Es j, pero es mejor este
        'Z': '2',
        ' ': ' ', #Agrego el espacio.
        '0' :'0', #Agrego numeros y ñ
        '1' :'1',
        '2' :'2',
        '3' :'3',
        '4' :'4',
        '5' :'5',
        '6' :'6',
        '7' :'7',
        '8' :'8',
        '9' :'9',
        'ñ' : 'ñ' #Aguante el espaÑol! 
        }

        texto_modificado = str()
        #print(texto_modificado)
        for letra in range(0,len(texto)):
                for key in leet_dict:
                        #print(key)
                        if texto.upper()[letra] == key:
                                texto_modificado += leet_dict[key]
                               # texto_modificado[letra] = leet_dict[key] No se puede reemplazar un solo char.
        return texto_modificado

texto_a_convertir = input("Hola, ingrese un texto para pasarlo a formato leet: ")
input(convertidor_hacker(texto_a_convertir))
                


