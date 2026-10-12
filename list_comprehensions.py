tickets = [
    {"categoria": "bug", "urgencia": "alta"},
    {"categoria": "acceso", "urgencia": "baja"},
    {"categoria": "bug", "urgencia": "alta"},
]

urgencias = ["baja", "alta", "media", "alta", "baja"]
mayusculas = [urgencia.upper() for urgencia in urgencias]
solo_altas = [urgencia for urgencia in urgencias if urgencia == "alta"]
categorias_urgentes = [ticket["categoria"] for ticket in tickets if ticket["urgencia"] == "alta"]
def clasificar_urgencia(texto, umbral="media"):
    return(f"Texto: {texto}, umbral mínimo: {umbral}") 

resultado1 = clasificar_urgencia("no puedo entrar")
resultado2 = clasificar_urgencia("no puedo entrar", "alta")
print(resultado1)
print(resultado2)