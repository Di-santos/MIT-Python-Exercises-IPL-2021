def lend_money(dividas, pessoa, qtd):
    dividas.setdefault(pessoa, [])
    dividas[pessoa].append(qtd)
    return None

def amount_owed_by(dividas, pessoa):
    if pessoa not in dividas.keys():
        return 0
    else:
        return sum(dividas[pessoa])

def total_amount_owed(dividas):
    soma = 0
    for k, v in dividas.items():
        soma += sum(v)
    return soma
