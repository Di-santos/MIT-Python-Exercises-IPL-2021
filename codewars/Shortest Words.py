def find_short(frase):
    menorPalavra = 1000

    for palavra in frase.split():
        if len(palavra) < menorPalavra:
            menorPalavra = len(palavra)

    return menorPalavra


print(find_short("bitcoin take over the world maybe who knows perhaps"))


#test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
#test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
#test.assert_equals(find_short("lets talk about javascript the best language"), 3)