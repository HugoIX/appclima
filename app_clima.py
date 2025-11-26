import requests

ciudad = input("Ingrese una ciudad: ").title()

fuente = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=es&appid=16bb858c02f9b349a7b5f4f0077ebea9&units=metric".format(ciudad)

res = requests.get(fuente)

data = res.json()

if res.status_code == 200:
    data = res.json()

    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    rain = data.get("rain", {}.get("1h", 0))
    clouds = data["clouds"]["all"]

    description = data["weather"][0]["description"]

    print(f"INFORME DEL CLIMA EN: {ciudad}")
    print("Ciudad: ", data["name"])
    print("Temperatura: ", temp, "°C")
    print("Temperatura Mínima/Máxima: ", temp_min, "°C", "  /  ", temp_max, "°C")
    print("Pronostico de lluvia (Última Hora): ", rain, "mm")
    print("Nubosidad: ", clouds, "%")
    print("Descripción: ", description.capitalize())

else:
    print(f"Error al obtener los datos de la capa: {res.status_code}.")
    print("Asegúrese de que la ciudad sea válida.")