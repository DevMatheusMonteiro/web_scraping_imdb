from .scraping_config import soup_imdb_movies
from models.movie import Movie

soup = soup_imdb_movies()
movie = Movie()

def extrair_filmes(limit=0):
    lista = soup.find("ul", class_="ipc-metadata-list")
    for li in lista.find_all("li", class_="ipc-metadata-list-summary-item", limit=limit):
        titulo = li.find("h3").text.split(".")[1].strip()
        ano = li.find("span", class_="cli-title-metadata-item").text.strip()
        nota = li.find("span", class_="ipc-rating-star--rating").text.strip()
        print(f"{titulo} ({ano}) - Nota: {nota}")