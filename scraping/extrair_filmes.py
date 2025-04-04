from .scraping_config import soup_imdb_movies
from models.movie import Movie
from services.movie_service import MovieService
from utils.app_error import AppError

soup = soup_imdb_movies()

def extrair_filmes(limit=None):
    movies = []
    lista = soup.find("ul", class_="ipc-metadata-list")
    for li in lista.find_all("li", class_="ipc-metadata-list-summary-item", limit=limit):
        title = li.find("h3").text.split(".")[1].strip()
        span = li.select("span.cli-title-metadata-item")
        year = span[0].text.strip()
        rating = li.find("span", class_="ipc-rating-star--rating").text.strip()
        runtime = span[1].text.strip()
        movies.append(Movie(title=title, year=year, rating=float(rating), runtime=runtime))
    return movies
def exibir_filmes(movies):
    for movie in movies:
        print(movie.__str__() + "\n*************")
def criar_filmes(movies):
    for movie in movies:
        try:
            movie_id = MovieService.create_movie(movie.to_dict())
            print(f"Filme com o id {movie_id} adicionado com sucesso.")
        except AppError as e:
            print(f"Erro: {e.message}")
        except Exception as e:
            print(f"Um erro inesperado aconteceu: {e}")