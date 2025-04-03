import urllib.request
from bs4 import BeautifulSoup

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def soup_imdb_movies():
    request_movies = urllib.request.Request("https://www.imdb.com/chart/top/", headers=headers)
    html_movies = urllib.request.urlopen(request_movies).read()
    return BeautifulSoup(html_movies, "html.parser")
def soup_imdb_series():
    request_series = urllib.request.Request("https://www.imdb.com/chart/toptv/", headers=headers)
    html_series = urllib.request.urlopen(request_series).read()
    return BeautifulSoup(html_series, "html.parser")