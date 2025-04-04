from scraping.exibir_filmes import exibir_detalhes_filmes, exibir_titulos_filmes
from scraping.extrair_filmes import extrair_filmes, exibir_filmes, criar_filmes
from scraping.extrair_series import extrair_series, exibir_series, criar_series
from database.database_config import create_tables
# 1. Extrair os filmes do ranking do IMDb
# exibir_titulos_filmes(10)
# print("******************")
# 2. Extrair título, ano e nota do IMDb
# exibir_detalhes_filmes(5)

# 4 - Criar uma lista de objetos Movie e Series a partir de scraping
movies = extrair_filmes()
# exibir_filmes(movies)
series = extrair_series()
# exibir_series(series)

create_tables()

criar_filmes(movies)
criar_series(series)