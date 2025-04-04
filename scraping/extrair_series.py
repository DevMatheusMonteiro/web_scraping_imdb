from .scraping_config import soup_imdb_series
from models.series import Series
from services.serie_service import SerieService
from utils.app_error import AppError

soup = soup_imdb_series()

def extrair_series(limit=None):
    series = []
    lista = soup.find("ul", class_="ipc-metadata-list")
    for li in lista.find_all("li", class_="ipc-metadata-list-summary-item", limit=limit):
        title = li.find("h3").text.split(".")[1].strip()
        span = li.select("span.cli-title-metadata-item")
        span_ano = span[0].text.replace("–", "-").strip()
        year = span_ano.split("-")[0].strip()
        rating = li.find("span", class_="ipc-rating-star--rating").text.strip()
        seasons = span_ano
        episodes =span[1].text.split()[0].strip()
        series.append(Series(title=title, year=year, rating=rating, seasons=seasons, episodes=episodes))
    return series
def exibir_series(series):
    for serie in series:
        print(serie.__str__() + "\n*************")
def criar_series(series):
    for serie in series:
        try:
            serie_id = SerieService.create_serie(serie.to_dict())
            print(f"Série com o id {serie_id} adicionado com sucesso.")
        except AppError as e:
            print(f"Erro: {e.message}")
        except Exception as e:
            print(f"Um erro inesperado aconteceu: {e}")