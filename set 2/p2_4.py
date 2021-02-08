def largest_number (listanum): 
    if len(listanum) == 0 or len(listanum) == 1:
        return None

    else:
        maior = -100 ** 9
        for i in listanum:
            if i > maior:
                maior = i

    return maior

def second_largest_number(listanum):

    if len(listanum) == 0 or len(listanum) == 1:
        return None
    
    else:
        maior1 = largest_number(listanum)
        listanum.remove(maior1)
        maior2 = largest_number(listanum)
        return maior2
