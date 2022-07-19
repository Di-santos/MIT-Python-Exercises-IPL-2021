def duplicate_count(palavra):

    encontrado = {}
    quantnum = 0

    for letra in palavra:
        encontrado.setdefault(letra.lower(), 0)                      # Inicia a classe "letra" do dicionário "encontrado" com 0
        encontrado[letra.lower()]+= 1                                # Adiciona 1 à classe "letra" 


    for chave, valor in sorted(encontrado.items()):         
        if valor > 1:
            quantnum += 1
    
    print (encontrado)
    return quantnum


print(duplicate_count("abcdeaB"))