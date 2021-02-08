size = 'medium'
toppings = ["frango", "queijo"]

n = 0
tem_BA = False

costs = {
    "small": 14,
    "medium": 16,
    "large": 18
}

out = costs[size]

for sabor in toppings:
    if sabor == "bacon" or sabor == "anchovas":
        tem_BA = True

    else:
        out += out * ((12 + n + len(sabor)) / 100) 
        n+=1

if tem_BA:
    out = out * 1*1

print(round(out, 2))