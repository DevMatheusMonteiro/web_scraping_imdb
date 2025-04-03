from database.database_config import Base, sql
class TV(Base):
    __tablename__ = "tv"

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    title = sql.Column(sql.String, nullable=False, unique=True)
    year = sql.Column(sql.DateTime, nullable=False)
    rating = sql.Column(sql.Float, nullable=False, default=0)
    type = sql.Column(sql.String, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "tv",
        "polymorphic_on": type
    }

    def __str__(self):
        return f"Título: {self.title}\nAno de Lançamento: {self.year}\nNota no IMDb: {self.rating}"