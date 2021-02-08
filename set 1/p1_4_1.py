poly = [0, 0, 1/2]
out = []

for i in range(1, len(poly)):
    if i == 1:
        out.append(int(poly[i]))
    
    else:
        out.append(int(poly[i] * i))
    
print(out)