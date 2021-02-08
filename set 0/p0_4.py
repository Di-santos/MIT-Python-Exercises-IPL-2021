import math

year = 1996
month = 7
day = 3

if month <= 2:
    month+= 12

if month <= 2:
    year -= 1

out = (day + math.floor((13 * (month + 1)) / 5) + year + math.floor(year / 4) - math.floor(year / 100) + math.floor(year / 400)) % 7

print (out)