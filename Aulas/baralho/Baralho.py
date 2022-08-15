from Carta import Carta
import random
class Baralho:
    def __init__(self):
        self.container = list()
        naipe = ['ouro','espada','copa','paus']
        cor = ['vermelho','preto','vermelho','preto']
        valor = ['As','2','3','4','5','6','7','8','9','10','valete','dama','rei']

        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.container.append(Carta(valor[v],naipe[n],cor[n]))

    def __str__(self):
        s = ''
        for carta in self.container:
            s += (carta.__str__() + '\n')
        return s

    def __len__(self):
        return len(self.container)

    def embaralhar(self):
        random.shuffle(self.container)
