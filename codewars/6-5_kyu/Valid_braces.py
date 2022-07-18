from enum import Flag
from re import A
from reprlib import aRepr


def valid_braces(string: str):
    opened = ["(", "[", "{"]
    closed = [")", "]", "}"]

    found = []

    for i, brace in enumerate(string):
        # se aberto, adiciona no found dict
        if brace in opened:
            found.append(brace)
        
        # se não
        else:
            # verifica se da match no último aberto
            bracePair = opened[closed.index(brace)]

            if len(found) > 0 and bracePair == found[-1]:
                found.pop()

    return True if found == [] else False

    

print(valid_braces(")(}{]["))