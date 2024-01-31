"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""
 
def contador_partido (lista_puntos): #Voy a hacer entrada con una lista, para más comodidad.
    var1,var2 = 0,0
    dic_puntos = { #Utilizo un dict para facilitar el seguimiento de los puntos.
        0:"Love",
        1 : 15,
        2 : 30,
        3: 40
    }
    for punto in lista_puntos:
        if punto == "P1" or punto == "p1": #Sumo los puntos
            var1+=1
        else:
            var2+=1
        if (var1 == var2) and var1>=3: #Si van iguales y alguno de los dos van >3(40) estan en deuce
            print("Deuce")
        elif var1>3  and (var1-var2==1):#Aca uso abs para saber la diferencia entre ambos  
            print("Ventaja para P1")         #Si es uno y ya tienen mas de 3 puntos(40) alguno esta en ventaja
        elif var2>3  and (var2-var1==1):
            print("Ventaja para P2") 
        elif var1>3 and (var1-var2==2): #Ya tiene mas de 3(40) y hay Diferencia de +2 es Victoria
            resultado = "Gano el jugador P1"
        elif var2>3 and (var2-var1==2):
            resultado = "Gano el jugador P2"
        else:                               #Si no se da ninguna situacion es que no pasaron los 40pts.
            print(f'{dic_puntos[var1]} - {dic_puntos[var2]} ') #Aca el dict me simplifica los primeros prints.
    print(resultado)
contador_partido(["P1","P1","P2","P2","P1","P2","P1","P2","P2","P2"])



                                                                 






