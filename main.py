import requests
from bs4 import BeautifulSoup

url = "https://www.laposte.fr/professionnel/la-carte-pro"

response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Erreur HTTP {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("title").text
print(f"Titre de la page : {title}")
