from repositories.serie_repository import SerieRepository, Series
from utils.app_error import AppError
class SerieService():
    @staticmethod
    def create_serie(data):
        title = data.get("title")
        year = data.get("year")
        rating = data.get("rating")
        seasons = data.get("seasons")
        episodes = data.get("episodes")
        if not title:
            raise AppError(message="Título é obrigatório.")
        if not year:
            raise AppError(message="Ano é obrigatório.")
        if not rating:
            raise AppError(message="Nota é obrigatória.")
        if not seasons:
            raise AppError(message="Temporada é obrigatório.")
        if not episodes:
            raise AppError(message="Episódio é obrigatório.")
        find_by_title = SerieRepository.find_serie_by_title(title)
        if find_by_title:
            raise AppError(message="Série já registrada.")
        serie_id = SerieRepository.create_serie(Series(title=title, year=year, rating=rating, seasons=seasons, episodes=episodes))
        return serie_id