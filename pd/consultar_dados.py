import pandas as pd
import os
from database.database_config import engine, sql

select_movies = """
SELECT m.id, tv.title, tv.year, tv.rating, m.runtime
FROM movies m
INNER JOIN tv ON tv.id = m.id"""
select_series = """
SELECT s.id, tv.title, tv.year, tv.rating, s.seasons, s.episodes
FROM series s
INNER JOIN tv ON tv.id = s.id"""

def consultar_dados():
    try:
        df_movies = pd.read_sql(select_movies, con=engine)
        df_series = pd.read_sql(select_series, con=engine)
        print("Movies:")
        print(df_movies.head())
        print("Series:")
        print(df_series.head())
    except Exception as e:
        print(f"Erro ao consultar o banco: {e}")
def analisar_filmes():
    try:
        df_movies = pd.read_sql(select_movies, con=engine)
        df_sorted = df_movies.sort_values(by="rating", ascending=False)
        df_top_movies = df_sorted[df_sorted["rating"] > 9.0]
        print("Top 5 Filmes Mais Bem Avaliados:")
        print(df_top_movies.head())
    except Exception as e:
        print(f"Erro ao consultar o banco: {e}")
def exportar_dados():
    data_path = f"{os.getcwd()}\\data"
    try:
        df_movies = pd.read_sql(select_movies, con=engine)
        df_series = pd.read_sql(select_series, con=engine)
        df_movies.to_csv(f"{data_path}\\movies.csv", index=False, encoding="utf-8")
        df_series.to_csv(f"{data_path}\\series.csv", index=False, encoding="utf-8")
        df_movies.to_json(f"{data_path}\\movies.json", orient="records", indent=4, force_ascii=False)
        df_series.to_json(f"{data_path}\\series.json", orient="records", indent=4, force_ascii=False)
    except Exception as e:
        print(f"Erro ao exportar os dados: {e}")