def order(frase):
    numeros = []
    dicOrdem = {}

    for i in range(101):
        numeros.append(str(i))

    for palavra in frase.split():
        for letra in palavra:
            if letra in numeros:
                dicOrdem[palavra] = int(letra)

    return" ".join(dict(sorted(dicOrdem.items(), key=lambda item: item[1])).keys())


print(order("4of Fo1r pe6ople g3ood th5e the2"))

#Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
#Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
#Test.assert_equals(order(""), "")