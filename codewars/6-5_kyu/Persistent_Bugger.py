# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

from typing import List


def persistence(n):
    last = n
    steps = 0

    def multiplyList(myList: List[str]) :
        result = 1
        for x in myList:
            result = result * int(x)
        print("RESULTADO: " + str(result))
        return result

    while len(str(last)) != 1:
        print(last)
        res = multiplyList(list(str(last)))
        last = res
        steps+=1

    return steps

print(persistence(39))