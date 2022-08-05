from urllib.request import urlopen
from bs4 import BeautifulSoup

# Passa a url para a request
url = "http://olympus.realpython.org/profiles/aphrodite"
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
title = data.find_all("img")
print(title)