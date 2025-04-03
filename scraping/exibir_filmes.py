from .scraping_config import soup_imdb_movies
soup = soup_imdb_movies()
def exibir_titulos_filmes(limit=0):
    lista = soup.find("ul", class_="ipc-metadata-list")
    for li in lista.find_all("li", class_="ipc-metadata-list-summary-item", limit=limit):
        print(li.find("h3").text)
def exibir_detalhes_filmes(limit=0):
    lista = soup.find("ul", class_="ipc-metadata-list")
    for li in lista.find_all("li", class_="ipc-metadata-list-summary-item", limit=limit):
        titulo = li.find("h3").text.split(".")[1].strip()
        ano = li.find("span", class_="cli-title-metadata-item").text.strip()
        nota = li.find("span", class_="ipc-rating-star--rating").text.strip()
        print(f"{titulo} ({ano}) - Nota: {nota}")