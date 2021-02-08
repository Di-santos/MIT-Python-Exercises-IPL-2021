a = 4
b = 5
c = 12

delta = b**2 - 4*a*c

if delta == 0:
    out = -b / (2*a)

else:
    x1 = (-b + (delta ** 0.5)) / (2*a)
    x2 = (-b - (delta ** 0.5)) / (2*a)
    out = x1, x2

print(out)
