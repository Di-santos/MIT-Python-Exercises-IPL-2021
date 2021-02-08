numbers = [3, 4, 12, 9, 7]

if len(numbers) == 0:
    out = "None"

else:
    soma = 0
    for numero in numbers:
        soma += numero

    out = soma/len(numbers)

print(out)

    
