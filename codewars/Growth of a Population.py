import math

def nb_year(popInicial, porcentagemAno, aumentoFlat, popAlvo):
    anos = 0

    while(popInicial < popAlvo):
        anos += 1
        popInicial = math.floor(popInicial + (popInicial * porcentagemAno/100) + aumentoFlat)
        print(popInicial)
    
    return anos





print(nb_year(1000, 2, 50, 1200))

#Test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
#Test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
#Test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)