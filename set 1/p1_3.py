dividend = 7
divisor = 2

num = divisor
quociente = 1
resto = 0


while num < dividend:
    if (num + divisor) > dividend:
        resto = dividend - num
        break

    else:
        num += divisor
        quociente += 1
        print(num) 

out = (quociente, resto)
print(out)