import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["agudo", "artritis", "ataxia", "atrofia", "conducta", "contractura", "distrofia", "dosis", "espasticidad", "excremento", "fisioterapeuta", "funcional", "genetica", "hemiplejia", "herencia", "higiene", "infantil", "imitar", "juvenil", "ligamento", "mental", "miembro", "nervio", "ocupacional", "pantorrilla", "plaguicidas", "postura", "procedimiento", "progresivo", "retraso", "social", "terapia", "trasladar", "tronco", "vacuna", "vejiga", "velcro", "virus"]

chosen_word = random.choice(word_list)
#print(chosen_word)

# Creación de una variable con el mismo numero de espacios que letras tiene la palabra elegida

word_lenght = ""
for len in chosen_word:
    word_lenght += "_"
print("La palabra a adivinar: {}".format(word_lenght))

# Se utiliza un bucle while para que el usuario siga jugando.
correct_word = False
guess_list = []
lives = 6
while not correct_word:
    print("****************************TE QUEDAN {} VIDAS****************************".format(lives))
    guess = input("Elige una letra: ").lower()
    
    #Se avisa al usuario si elige la misma letra que en un intento anterior
    if guess in guess_list:
        print ("Ya has elegido la letra {}".format(guess))

    display = ""
# Se utiliza un bucle for que coloque en la posición correcta las letras acertadas

    for letter in chosen_word:

        if letter == guess:
            display += letter
    # Se guardan las letras acertadas en una lista para mantener en el sitio adecuado todas las letras acertadas  
            guess_list.append(guess)
        elif letter in guess_list:
            display += letter
        else:
            display += "_"

    print("La palabra a adivinar: " + display)

    # Si la letra no se encuentra en la palabra a adivinar, se pierde una vida.
    if guess in guess_list:
        print("¡Bien!")
    else:
        lives -= 1
        print ("¡Error! La letra {} no está en la palabra que buscas. Pierdes 1 vida".format(guess))

    #Se muestra el clasico dibujo del ahorcado, avanzando en función de las vidas que quedan
    print (stages[lives])

    # Si se acaban las vidas, el juego termina y pierdes         
    if lives == 0:
        print("*********************** PERDISTE **********************\n La palabra era {}.".format(chosen_word))
        break

    #Si la palabra coincide, ganas el juego
    if display == chosen_word:
        print("**************************** ¡ENHORABUENA! ¡HAS GANADOO! ****************************")
        correct_word = True
    #Si quedan espacios por rellenar y te quedan vidas, sigues jugando
    else:
        print("Sigue intentandolo")

