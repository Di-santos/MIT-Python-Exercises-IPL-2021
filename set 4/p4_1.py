def warehouse_process(armazem, fluxo):
    if fluxo[0] == 'receive':
        if fluxo[1] in armazem.keys():
            armazem[fluxo[1]] += fluxo[2]
        else:
            armazem[fluxo[1]] = fluxo[2]
    
    elif fluxo[0] == 'ship':
        if armazem[fluxo[1]] - fluxo[2] < 0:
            armazem[fluxo[1]] = 0
            print('not enough')
        else:
            armazem[fluxo[1]]-= fluxo[2]

class Warehouse():
    def __init__(self):
        self.armazem = {}

    def process(self, fluxo):
        if fluxo[0] == 'receive':
            if fluxo[1] in self.armazem.keys():
                self.armazem[fluxo[1]] += fluxo[2]
            else:
                self.armazem[fluxo[1]] = fluxo[2]
    
        elif fluxo[0] == 'ship':
            if self.armazem[fluxo[1]] - fluxo[2] < 0:
                self.armazem[fluxo[1]] = 0
                print('not enough')
            else:
                self.armazem[fluxo[1]]-= fluxo[2]

    def lookup(self, produto):
        if produto in self.armazem.keys():
            return self.armazem[produto]
        else:
            return 0
