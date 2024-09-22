nombre1 = input("¿Cual es tu nombre?: ")
nombre2 = input("¿Cual es tu nombre?: ")

piedra = "piedra"
papel = "papel"
tijeras = "tijeras"

correcto = False
cant_jugadas = 0
score_jug1 = 0
score_jug2 = 0

while cant_jugadas <= 5: 
    print(nombre1 , "¿Que eliges? ¿Piedra, Papel o Tijeras?: ") 
    jugador1 = input()
    jugador1_correg = str(jugador1).strip().lower()

    if jugador1_correg == piedra or jugador1_correg == papel or jugador1_correg == tijeras:
        correcto = True

    while not correcto:
        jugador1 = input("La selección fue erronea, ¿Que eliges? ¿Piedra, Papel o Tijeras?: ")
        jugador1_correg = str(jugador1).strip().lower()
        if jugador1_correg == piedra or jugador1_correg == papel or jugador1_correg == tijeras:
            correcto = True
    else:
        correcto = False

    print(nombre2 , "¿Que eliges? ¿Piedra, Papel o Tijeras?: ") 
    jugador2 = input()
    jugador2_correg = str(jugador2).strip().lower()

    if jugador2_correg == piedra or jugador2_correg == papel or jugador2_correg == tijeras:
        correcto = True

    while not correcto:
        jugador2 = input("La selección fue erronea, ¿Que eliges? ¿Piedra, Papel o Tijeras?: ")
        jugador2_correg = str(jugador2).strip().lower()
        if jugador2_correg == piedra or jugador2_correg == papel or jugador2_correg == tijeras:
            correcto = True

    else:
        correcto = False

    condicion1 = jugador1_correg == "piedra" and jugador2_correg == "tijeras"
    condicion2 = jugador1_correg == "papel" and jugador2_correg == "piedra"
    condicion3 = jugador1_correg == "tijeras" and jugador2_correg == "papel"


    if jugador1_correg == jugador2_correg:
        cant_jugadas += 1
        print("¡¡ Ha sido un empate !!")
    elif condicion1 or condicion2 or condicion3:
        cant_jugadas += 1
        score_jug1 += 1
        print("¡¡ Ha ganado el punto", nombre1, "!!")
    else:
        cant_jugadas += 1
        score_jug1 += 1
        print("¡¡ Ha ganado el punto", nombre2, "!!")
else:
    if score_jug1 == score_jug2:
        print("¡¡ Ha sido un empate !!", score_jug1, "a", score_jug2)
    elif score_jug1 > score_jug2:
        print("¡¡ Ha ganado", nombre1, "!!,", score_jug1, "a", score_jug2)
    else:
        print("¡¡ Ha ganado", nombre2, "!!", score_jug2, "a", score_jug1)