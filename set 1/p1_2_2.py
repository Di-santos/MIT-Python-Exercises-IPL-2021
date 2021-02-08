numbers = [2,4,10]

if len(numbers) == 0:
    out = "None"

else:
    produto = 1
    for numero in numbers:
        produto = produto * numero

    out = produto ** (1/len(numbers))

print(out)

    
