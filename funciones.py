def saludar(nombre):
    print("Hola", nombre, "Bienvenido a Atlas Academy")
def es_mayor_de_edad(edad):
    return edad >= 18
saludar("Santiago")
resultado = es_mayor_de_edad(20)
print(resultado)