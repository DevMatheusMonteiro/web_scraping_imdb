from database.database_config import sql
from .tv import TV

class Movie(TV):
    __tablename__ = "movies"

    id = sql.Column(sql.Integer, sql.ForeignKey("tv.id", ondelete="CASCADE"), primary_key=True)
    rating = sql.Column(sql.Float, nullable=False, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "movies"
    }

    def __str__(self):
        return f"{super().__str__()}\nNota no IMDb: {self.rating}"