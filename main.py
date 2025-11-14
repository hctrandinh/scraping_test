import requests
from bs4 import BeautifulSoup

url = "https://www.laposte.fr/professionnel/la-carte-pro"

# Définir un User-Agent pour ressembler à un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise Exception(f"Erreur HTTP {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("title").text
print(f"Titre de la page : {title}")
