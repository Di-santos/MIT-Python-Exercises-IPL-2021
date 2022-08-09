from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter

# Localiza e instancia o driver com o path pro driver no navegador
PATH = "/home/dyokinn/chromedriver"
user = input("RA: ")
password = input("SENHA: ")

driver = webdriver.Chrome(PATH)

# Acessa
driver.get("https://sistemas.dac.unicamp.br/siga/mobile/signin")

notas = WebDriverWait(driver, 10000).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )

driver.find_element(By.ID, "username").send_keys(user)
driver.find_element(By.ID, "password").send_keys(password)

driver.find_element(By.ID, "signin-confirmar").click()


try:
    # Checa se carregou as estrofes
    notas = WebDriverWait(driver, 10000).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "menu_item"))
    )
    print(len(notas))
    notas[1].click()
    print("clicou")
    # Puxa código das notas
    codes = WebDriverWait(driver, 10000).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "MuiTypography-root.MuiTypography-body1.MuiTypography-gutterBottom.css-1tqv6h6"))
    )
    strCodes = [code.text for code in codes]

    # Puxa as notas em si
    grades = WebDriverWait(driver, 10000).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault.css-iieutf"))
    )
    strGrades = [grade.text for grade in grades]

    # Excel
    wb = xlsxwriter.Workbook('notas.xlsx')
    ws = wb.add_worksheet()
    for i, (code, grade) in enumerate(zip(strCodes, strGrades)):
        ws.write(i, 0, code)
        ws.write(i, 1, grade)
    wb.close()

except:
    print("deu pau")

driver.quit()