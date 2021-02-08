kwh_used = 1000

contKw = 0
valor = 0

while(contKw <= kwh_used):
    if contKw <= 500:
        contKw += 1
        valor += 0.45
    
    elif contKw <= 1500:
        contKw += 1
        valor += 0.74

    elif contKw <= 2500:
        contKw += 1
        valor += 1.25

    else:
        contKw += 1
        valor += 2

out = 1.2 * int(valor)
print(out)