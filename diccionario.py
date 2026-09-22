persona = {
    "nombre": "Santiago",
    "edad": 16,
    "curso": "Atlas Academy",
    "juego": "Albion Online"
}
print(persona["nombre"])
print(persona["edad"])
persona["ciudad"] = "Madrid"
for clave in persona:
    print(clave, ":", persona[clave]) 