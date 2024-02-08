"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""
def jankenpon(listado_jugada): #Se pueden jugar las rondas que se quieran.
    player1,player2= 0,0 #Para indicar los puntos de los jugadores.
    resultado = "" #Cadena vacia, para depositar que sucedio.
    reglas = { #Hago las reglas para cada caso, lo que se encuentra dentro, son contra los elementos que ganaría. Sino pierde.
        "🗿" : ["✂️","🦎"],
        "📄" : ["🗿","🖖"],
        "✂️" : ["📄","🦎"],
        "🦎" : ["📄","🖖"],
        "🖖" : ["✂️","🗿"]
    }
    #Esto de abajo funciona correctamente, pero me gusto más la implementacion de cgpt.
    # for i in range(len(listado_jugada)): #Hago un rango de las jugadas
    #     valores_que_gana = reglas.get(listado_jugada[i][0])#El Get me devuelve Los valores asociados, es decir, contra lo que gana el primer elemento (0), que sera player1
    #     if valores_que_gana[0] == valores_que_gana[1]:
    #         player1+=0
    #         player2+=0
    #     elif valores_que_gana[0] == listado_jugada[i][1] or valores_que_gana[1] == listado_jugada[i][1]: #listado_jugada[i][1] Es el valor de la derecha o sea, player2
    #         player1 += 1  #Si se encuentra, El P1 le gano a P2, un punto. Entonces le sumo 1 a P1
    #     else:
    #         player2 += 1 #Si no se encuentra, El P2 le gano a P1, un punto. Entonces le sumo 1 a P2

    for jugada in listado_jugada: #Asi lo hace cgpt, mas sencillo, recorriendo el dict directamente en las condiciones
        if jugada[0] in reglas and jugada[1] in reglas[jugada[0]]:
            player1 += 1
        elif jugada[1] in reglas and jugada[0] in reglas[jugada[1]]:
            player2 += 1
    if player1 == player2:
        resultado = "Empate"
    if player1>player2:
        resultado = "Gano el Player 1"
    else:
        resultado = "Gano el Player 2"
    return resultado

listado_jugada = [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]
resultado = jankenpon(listado_jugada)
print(resultado)








