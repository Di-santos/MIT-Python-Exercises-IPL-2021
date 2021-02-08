p_d = 5
in_circle = 0
positions = []

for y in range( round(p_d/2), (round(-p_d/2) - 1), -1):
    for x in range(round(-p_d/2), round(p_d/2) + 1):
        if (x**2 + y**2) ** 0.5 <= p_d/2:
            in_circle += 1

out = (in_circle/(p_d**2)) * 4

print(out)