print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("¡Bienvenido a la Isla del Tesoro!")
print("Tu misión es encontrar el tesoro.")
first_decision = input("¿Deberías girar a la derecha o a la izquierda?\n").lower()
if first_decision != "izquierda":
    print( "Te has caido a un agujero. Se acabó el juego.")
else:
    second_decision = input("Llegas a un lago. ¿Nadas o esperas?\n").lower()
    if second_decision != "espero":
        print("Te atacan un puñado de tiburones. Se acabó el juego")
    else:
        third_decision = input("Tienes delante tres puertas. ¿Qué puerta eliges? ¿Roja, azul o amarilla?\n").lower()
        if third_decision == "roja":
            print("Te achicharra una bola de fuego. Se acabó el juego")
        elif third_decision == "azul":
            print( "Te come una bestia. Se acabó el juego")
        elif third_decision == "amarilla":
            print("Enhorabuena. ¡Has ganado!")
        else:
            print("{} no es una opción, cobarde. Se acabó el juego para ti también.".format(third_decision))