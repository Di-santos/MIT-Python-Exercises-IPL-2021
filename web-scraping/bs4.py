from urllib.request import urlopen
from bs4 import BeautifulSoup

# Passa a url para a request
url = "https://www.letras.mus.br/duzz-mc/"
page = urlopen(url)

# Extrai o HTML da página
html_bytes = page.read()
html = html_bytes.decode("utf-8")
data = BeautifulSoup(html, "html.parser")

# Sem parser
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

# Com parser
title = data.find_next("title")

# Puxando nomes de músicas de artistas
musics = []
for li in data.find_all("li" , attrs={"class": "cnt-list-row -song"}):
    musics.append(li.contents[1].contents[0].contents[0])

print(musics)