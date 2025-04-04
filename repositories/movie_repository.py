from database.database_config import session
from models.movie import Movie
class MovieRepository():
    @staticmethod
    def create_movie(movie):
        session.add(movie)
        session.commit()
        session.refresh(movie)
        return movie.id
    @staticmethod
    def find_movie_by_title(title):
        return session.query(Movie).filter(Movie.title == title).first()