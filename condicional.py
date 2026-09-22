edad = int(input("¿Cuántos años tienes? "))
if edad < 13:
    print("Eres niño/a.")
elif edad >= 13 and edad <= 17:
    print("Eres adolescente.")
else:
    print("Eres adulto/a.")