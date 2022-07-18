import math

def find_next_square(number):
    if str(math.sqrt(number)).endswith('.0'):
        return (math.sqrt(number) + 1) * (math.sqrt(number) + 1)
    else:
        return -1

print(find_next_square(144))

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect