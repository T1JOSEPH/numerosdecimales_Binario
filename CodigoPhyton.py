#Tarea Phyton 

decimal=int(input("Ingresa un número decimal de 2 digitos porfavor: "))

valores=[128, 64, 32, 16, 8, 4, 2, 1]
binario=""
restante=decimal

for valor in valores:
    if restante >= valor:
        binario += "1"
        restante -= valor
    else:
        binario += "0"

print(f"El número {decimal} en binario de 8 bits es: {binario}")
