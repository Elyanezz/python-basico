import requests
respuesta = requests.get(
    "https://api.github.com/search/users",
    params={"q": "octocat"}
)
print(respuesta.status_code)
datos = respuesta.json()
print(datos["items"]["login"])