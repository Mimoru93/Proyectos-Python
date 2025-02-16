#Creación de calculadora para pago compartido, incluida la propina

print("¡Bienvenido a la calculadora de propinas!")
bill = float(input("¿Cuál es el total de la cuenta?\n"))
tip = int(input("¿Qué porcentaje te gustaría dar? 10, 12 o 15 \n"))
people = int(input("¿Entre cuantas personas vais a dividir la cuenta? \n"))
each_bill = round(bill/people*((100+tip)/100),2)
print("Cada uno debe poner {}€".format(each_bill))

