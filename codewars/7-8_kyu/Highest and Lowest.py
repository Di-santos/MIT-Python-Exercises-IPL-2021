def high_and_low(numString):
    numInt = []

    for numero in numString.split():
        numInt.append(int(numero))

    return str(max(numInt)) + " " + str(min(numInt))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

#Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");