from repositories.movie_repository import MovieRepository, Movie
from utils.app_error import AppError
class MovieService():
    @staticmethod
    def create_movie(data):
        title = data.get("title")
        year = data.get("year")
        rating = data.get("rating")
        runtime = data.get("runtime")
        if not title:
            raise AppError(message="Título é obrigatório.")
        if not year:
            raise AppError(message="Ano é obrigatório.")
        if not rating:
            raise AppError(message="Nota é obrigatória.")
        if not runtime:
            raise AppError(message="Duração é obrigatória.")
        find_by_title = MovieRepository.find_movie_by_title(title)
        if find_by_title:
            raise AppError(message="Filme já registrado.")
        movie_id = MovieRepository.create_movie(Movie(title=title, year=year, rating=rating, runtime=runtime))
        return movie_id