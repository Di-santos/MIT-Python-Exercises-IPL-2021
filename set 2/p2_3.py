def ndoors(num_portas):
    portas = {}
    portas_abertas = []
    passagem = 1
    for i in range(1, num_portas + 1):
        portas[i] = "trancada"
    
    while passagem < num_portas + 1:

        for i in range(1, num_portas + 1):
            if i % passagem == 0:
                if portas[i] == "trancada":
                    portas[i] = "aberta"
                else:
                    portas[i] = "trancada"
                
        passagem += 1   

    for key, val in portas.items():
        if val == "aberta":
            portas_abertas.append(key)

    return portas_abertas

print(ndoors(100))
