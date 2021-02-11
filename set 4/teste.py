def euclid_mdc(n1, n2):
    while n1 != 0:
        if n1 < n2:
            aux = n1
            n1 = n2
            n2 = aux
        
        n1-= n2
    
    return n2

