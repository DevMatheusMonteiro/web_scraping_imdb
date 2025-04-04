from database.database_config import session
from models.series import Series
class SerieRepository():
    @staticmethod
    def create_serie(serie):
        session.add(serie)
        session.commit()
        session.refresh(serie)
        return serie.id
    @staticmethod
    def find_serie_by_title(title):
        return session.query(Series).filter(Series.title == title).first()