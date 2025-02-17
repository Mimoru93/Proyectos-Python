#Creación de un programa automatico para pedir Pizza

#Presentación
print("Bienvenido a Python Pizza Deliveries!")

#Pedido
size = input("Qué tamaño de pizza quieres: pequeña (P), mediana (M) o grande(G)?\n").lower()
pepperoni = input("¿Quieres peperoni en la pizza? Sí(S) o No (N): \n").lower()
extra_cheese = input("¿Quieres extra de queso? Sí(S) o No (N): \n").lower()

#Factura
bill = 0
if size == "p":
    bill += 15
elif size == "m":
    bill += 20
elif size == "g":
    bill += 25
else:
    print("Has introducido una respuesta incorrecta.")

if pepperoni == "s":
    if size == "p":
        bill += 2
    else:
        bill += 3

if extra_cheese == "s":
    bill += 1

print("Tu pedido sale a {}€.".format(bill))
