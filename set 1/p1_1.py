interest_rate = 0.03

qAtual = 100
qAlvo = 200

anos = 0

if (interest_rate == 0):
    out = "NEVER"

else: 
    while (qAtual <= qAlvo):
        qAtual += qAtual * interest_rate
        anos += 1
    out = anos

print (out)
