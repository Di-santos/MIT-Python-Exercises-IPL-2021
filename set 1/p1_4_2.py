poly = [8, 4, 2]
const = 5
out = [const, poly[0]]

for i in range(1, len(poly)):
    out.append(poly[i] / (i + 1))

print(out)