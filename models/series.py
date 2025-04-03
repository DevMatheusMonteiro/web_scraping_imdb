from database.database_config import sql
from .tv import TV

class Series(TV):
    __tablename__ = "series"

    id = sql.Column(sql.Integer, sql.ForeignKey("tv.id", ondelete="CASCADE"), primary_key=True)
    seasons = sql.Column(sql.String, nullable=False)
    episodes = sql.Column(sql.Integer, nullable=False, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "series"
    }

    def __str__(self):
        return f"{super().__str__()}\nQuantidade de Temporadas: {self.seasons}\nQuantidade de Episódios: {self.episodes}"