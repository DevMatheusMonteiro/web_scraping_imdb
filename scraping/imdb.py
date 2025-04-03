import urllib.request
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


request = urllib.request.Request("http://www.imdb.com/chart/top/", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

html = urllib.request.urlopen(request).read()

soup = BeautifulSoup(html, "html.parser")

lista = soup.select("ul.ipc-metadata-list")[0]

for li in lista.select("li.ipc-metadata-list-summary-item", limit=10):
    print(li.find("h3").text)