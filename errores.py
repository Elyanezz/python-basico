try:
    numero = int(input("ingresa un número: "))
    doble = numero * 2
    print("El doble es:", doble)
except ValueError:
    print("Por favor, ingresa un número válido.")
