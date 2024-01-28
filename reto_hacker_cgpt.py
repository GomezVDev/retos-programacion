#Solucion de chat GPT en base a mi codigo
def convertidor_hacker(texto):
    leet_dict = {
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
        'L': '|_',
        'M': "|\/|",
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
        'Y': '`/',
        'Z': '2',
        ' ': ' ',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'ñ': 'ñ'
    }

    texto_modificado = '' #Es lo mismo que str()
    for letra in texto.upper():  #Simplemente lo hace así por lo que viene despues
        if letra in leet_dict:   #Había olvidado esta funcionalidad. C me traumo.
            texto_modificado += leet_dict[letra] #Aca y abajo lo hace igual que yo.
        else:
            texto_modificado += letra

    return texto_modificado

texto_a_convertir = input("Hola, ingrese un texto para pasarlo a formato leet: ")
print(convertidor_hacker(texto_a_convertir))


#Practicamente lo mismo pero fue mas eficiente en el loop, por haberme olvidado el in.