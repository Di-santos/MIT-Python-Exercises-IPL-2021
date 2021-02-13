class Matrix():
    def __init__(self, nums_list):
        self.linhas = nums_list
    
    def size(self):
        linhas = len(self.linhas)
        colunas = len(self.linhas[0])
        return (linhas, colunas)

    def get(self, i, j):
        return self.linhas[i][j]

    def set(self, i, j, val):
        self.linhas[i][j] = val

    def row(self,linha):
        return self.linhas[linha]

    def col(self, coluna):
        coluna_lista = []
        for linha in self.linhas:
            coluna_lista.append(linha[coluna])

        return coluna_lista

    def transpose(self):
        nova_mat = []

        for i in range(len(self.linhas[0])):
            nova_linha = []

            for linha in self.linhas:
                nova_linha.append(linha[i])

            nova_mat.append(nova_linha)

        return Matrix(nova_mat)

    def __add__(self, other):
        nova_mat = []

        if isinstance(other, Matrix) and self.size() == other.size():
            for i in (range(len(self.linhas))):
                novo_val = []

                for j in range(len(self.linhas[0])):
                    novo_val.append(self.linhas[i][j] + other.linhas[i][j])

                nova_mat.append(novo_val)

            return Matrix(nova_mat)
        
        elif isinstance(other, (int, float)):
            for i in (range(len(self.linhas))):
                novo_val = []

                for j in range(len(self.linhas[0])):
                    novo_val.append(self.linhas[i][j] + other)

                nova_mat.append(novo_val)

            return Matrix(nova_mat)
        
        else:
            return None

    def __sub__(self, other):
        nova_mat = []

        if isinstance(other, Matrix) and self.size() == other.size():
            for i in (range(len(self.linhas))):
                novo_val = []

                for j in range(len(self.linhas[0])):
                    novo_val.append(self.linhas[i][j] - other.linhas[i][j])

                nova_mat.append(novo_val)

            return Matrix(nova_mat)

        elif isinstance(other, (int, float)):
            for i in (range(len(self.linhas))):
                novo_val = []

                for j in range(len(self.linhas[0])):
                    novo_val.append(self.linhas[i][j] - other)

                nova_mat.append(novo_val)

            return Matrix(nova_mat)
        
        else:
            return None
        

