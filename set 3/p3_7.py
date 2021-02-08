def retorna_prox(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def hailstone_sequence(a_0):
    if a_0 == 1:
        return [a_0]
    
    else:
        valor_atual = a_0
        results = [valor_atual]

        while retorna_prox(valor_atual) != 1:
            results.append(retorna_prox(valor_atual))
            valor_atual = retorna_prox(valor_atual)
        
        results.append(1.0)
        return results

