import requests
respuesta = requests.get("https://api.github.com/users/octocat")
print(respuesta.status_code)
datos = respuesta.json()
print(datos["login"])
print(datos["location"])
print(datos["public_repos"])
print(datos["followers"])
print(datos["company"])