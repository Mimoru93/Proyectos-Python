#Importamos libreria
import random

#Creamos las variables de las tres opciones

rock = '''
Piedra
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Papel
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Tijeras
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Creamos lista de opciones
choises = [rock, paper, scissors]

#Creamos las variables del jugador y la maquina
player_choise = int(input("¿Qué eliges? Escribe 0 para Piedra, 1 para Papel y 2 para Tijeras:\n"))
computer_choise = random.randint(0,2)

#Mostramos las opciones elegidas por jugador y maquina
if player_choise >=0 and player_choise <=2:
    print("Tu eliges:\n", choises[player_choise])
    print("La maquina elige:\n", choises[computer_choise])

    #Creamos bucle con los posibles resultados
    if player_choise == 0 and computer_choise == 1:
        print("¡Perdiste!")
    elif player_choise == 1 and computer_choise == 2:
        print("¡Perdiste!")
    elif player_choise == 2 and computer_choise == 0:
        print("¡Perdiste!")
    elif player_choise == computer_choise:
        print("¡Empate!")
    else:
        print("¡Ganaste!")
#Filtro en caso de que el jugador elija otro numero que no esta entre las opciones.
else:
    print("Esto es Piedra, papel o tijeras, no Piedra, papel, tijeras, lagarto o Spock. Perdiste")

