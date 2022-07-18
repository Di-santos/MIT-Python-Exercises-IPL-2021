def solve(stringA,stringB):
    repeticoes = {}
    for palavra in stringB:
        repeticoes.setdefault(palavra, 0)
    
    for palavra in stringA:
        if palavra in stringB:
            repeticoes[palavra] +=1
    
    return list(repeticoes.values())







print(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']))

#Test.assert_equals(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
#Test.assert_equals(solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
#Test.assert_equals(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])