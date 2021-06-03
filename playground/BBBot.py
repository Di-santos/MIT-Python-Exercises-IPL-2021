# Karol = (588, 630)
# Captcha = (559, 476)
# Novamente = (647, 390)

import mouse
import time

def vota(votos):
    mouse.wheel(1)
    mouse.move(330, 518,3000)
    time.sleep(3)
    mouse.click('left')

    mouse.move(258, 646, 3000)
    time.sleep(2)
    mouse.click('left')

    mouse.move(367, 346, 3000)
    time.sleep(3)
    mouse.click('left')

    votos += 1

# ------------------------------------ CÓDIGO ----------------------------------------------------------
votos = 0
quant_votos = 30

while True:
    while votos < 5:
        vota(votos)
        votos += 1

    if votos == 5:
        time.sleep(35)
        votos = 0
    
    print(f' {quant_votos} votos computados!!!')


