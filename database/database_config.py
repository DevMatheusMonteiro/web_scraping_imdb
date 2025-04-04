import os
import sqlalchemy as sql
import sqlalchemy.orm as orm

engine = sql.create_engine(f"sqlite:///{os.getcwd()}\\database\\imdb.db")
Base = orm.declarative_base()
Session = orm.sessionmaker(bind=engine)
session = Session()

def create_tables():
    from models.movie import Movie
    from models.series import Series
    from models.tv import TV
    Base.metadata.create_all(engine)