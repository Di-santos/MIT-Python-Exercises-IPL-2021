from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Localiza e instancia o driver com o path pro driver no navegador
PATH = "/home/dyokinn/chromedriver"
driver = webdriver.Chrome(PATH)

# Acessa
driver.get("https://www.letras.mus.br/duzz-mc/")

# Pega as músicas (add "." onde tem espaço)
musics = driver.find_elements(By.CLASS_NAME, "cnt-list-row.-song")
musicNames = [music.get_attribute("data-name") for music in musics]

bars = []

for i in range(10):
    # Checa se o link tá clicável e clica
    a = WebDriverWait(driver, 10000).until(
            EC.element_to_be_clickable((By.LINK_TEXT, musicNames[i]))
        )
    a.click()

    try:
        # Checa se carregou as estrofes
        lyrics = WebDriverWait(driver, 10000).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "p"))
        )
        # Puxa versos
        versos = str(lyrics[0].text).split("\n")
        versos += str(lyrics[2].text).split("\n")
        bars += versos

        driver.back()
    except:
        print("Deu ruim")

bars = [bar + "\n" for bar in bars]
data = {
    "artista": "Duzz",
    "foto": "Duzz.jpg",
    "versos": bars
}

json_object = json.dumps(data, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

driver.quit()
