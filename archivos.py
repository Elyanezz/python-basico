with open("notas.txt", "w") as archivo:
    archivo.write("Me encanta mi baby")
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
