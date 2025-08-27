#### Vai ate o site do G1 e traz 10 títulos da página inicial ####

import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, "html.parser")

titulos = sopa.find_all("a", class_="feed-post-link", limit=10)

for i, t in enumerate(titulos, 1):
    print(f"{i}. {t.get_text(strip=True)}")
