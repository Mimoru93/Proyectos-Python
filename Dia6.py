import random

#Incorporamos las opciones
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Se inicia el programa preguntando al usuario
print("¡Bienvenido al generador de contraseñas de python!")
nr_letters = int(input("¿Cuántas letras quieres en tu contraseña?\n"))
nr_symbols = int(input(f"¿Cuántos símbolos quieres?\n"))
nr_numbers = int(input(f"¿Cuantos números quieres?\n"))

#Se seleccionan los caracteres
password_list = []
for let in range(0,nr_letters):
    password_list.append(random.choice(letters))
for sym in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for num in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

#Se aleatorizan
random.shuffle(password_list)

#Se muestra la contraseña
password = ""
for char in password_list:
    password += char
print("Tu contraseña podría ser", password)
