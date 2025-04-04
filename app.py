from scraping.exibir_filmes import exibir_detalhes_filmes, exibir_titulos_filmes
from scraping.extrair_filmes import extrair_filmes, exibir_filmes, criar_filmes
from scraping.extrair_series import extrair_series, exibir_series, criar_series
from database.database_config import create_tables
from pd.consultar_dados import consultar_dados, analisar_filmes, exportar_dados

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

# 5 - Criar um banco de dados SQLite e salvar os dados de filmes e séries
create_tables()
criar_filmes(movies)
criar_series(series)

# 6 - Consultar os dados do banco com Pandas
consultar_dados()

# 7 - Fazer uma análise de dados com Pandas
analisar_filmes()

# 8 - Exportando os dados para CSV e JSON
exportar_dados()