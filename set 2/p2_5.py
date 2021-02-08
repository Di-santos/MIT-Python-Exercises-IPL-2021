import string

def caesar_cipher(codigo, shift):
    caesar_base = {}
    count = 0
    novo_codigo = ''
    alfabeto = list(string.ascii_lowercase)
    digitos = list(string.digits)

    for letra in alfabeto:
        caesar_base[letra] = count
        count += 1

    for letra in codigo.lower() :

        if letra in alfabeto: 
            novo_i = caesar_base[letra] + shift

            if novo_i > 25:
                novo_i %= 26
                
            
            elif novo_i < 0:
                while novo_i < 0:
                    novo_i = 26 + novo_i
                
            key_letra = list(caesar_base.keys()) [list(caesar_base.values()).index(novo_i)]
            novo_codigo += key_letra

        elif letra in digitos:
            novo_i = int(letra) + shift

            if novo_i > 9:
                novo_i %= 10
            
            elif novo_i < 0:
                while novo_i < 0:
                    novo_i = 10 + novo_i
            
            novo_codigo += str(novo_i)
            
        else:
            novo_codigo += letra

    return novo_codigo
