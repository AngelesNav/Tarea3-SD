import requests
import json

entradas = [
    "Apple", "Samsung", "Google", "Microsoft", "Amazon",
    "Coca-Cola", "IBM", "Toyota", "McDonald's", "Disney",
    "Nike", "Adidas", "Pepsi", "Sony", "BMW",
    "Mercedes-Benz", "Volkswagen", "Ford", "General Electric", "Louis Vuitton",
    "Nestlé", "Intel", "Honda", "Sony Ericsson", "Canon Inc",
    "Siemens AG", "Panasonic", "Dell", "HP", "Oracle"
]

url = "https://es.wikipedia.org/w/api.php"  # versión en español
i = 1

for entrada in entradas:
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(url, params=params).json()

    # Manejo de la respuesta JSON
    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']

    # Escribir el texto en un archivo
    if i <= 15:
        with open(f'../carpeta1/{entrada}.txt', 'w', encoding='utf-8') as f:
            f.write(texto)
    else:
        with open(f'../carpeta2/{entrada}.txt', 'w', encoding='utf-8') as f:
            f.write(texto)
    i += 1

