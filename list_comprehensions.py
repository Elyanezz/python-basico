tickets = [
    {"categoria": "bug", "urgencia": "alta"},
    {"categoria": "acceso", "urgencia": "baja"},
    {"categoria": "bug", "urgencia": "alta"},
]

urgencias = ["baja", "alta", "media", "alta", "baja"]
mayusculas = [urgencia.upper() for urgencia in urgencias]
solo_altas = [urgencia for urgencia in urgencias if urgencia == "alta"]
categorias_urgentes = [ticket["categoria"] for ticket in tickets if ticket["urgencia"] == "alta"]