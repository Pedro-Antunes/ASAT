import random
from bitset import Bitset


class Individuo:

    def __init__(self, idt, valoracao):
        self._id = idt
        self._val = valoracao
        self._eval = None
        self._mem = []
        self._actv = Bitset(valoracao.getSize())
        self._PrMut = 0.5

    def getId(self):
        return self._id

    def getValoracao(self):
        return self._val

    def setValoracao(self, valoracao):
        self._val = valoracao
    
    def getEval(self):
        return self._eval

    def setEval(self, eval):
        self._eval = eval

    def memorize(self, valoracao):
        self._mem.append(valoracao)

    def getRandomMemVal(self):
        return random.choice(self._mem)

    def forget(self):
        self._mem.clear()

    def valCount(self):
        return len(self._mem)

    def uniqueValCount(self):
        uniqueValList = []  # Lista de valorações distintas
        for val in self._mem:
            found = False
            i = 0
            # Verifica se val é equivalente a alguma valoração de uniqueValList
            while not found and i < len(uniqueValList):
                if val.compare(uniqueValList[i]):
                    found = True
                i += 1
            # Adiciona esta valoração a uniqueValList se não encontrar equivalente
            if not found:
                uniqueValList.append(val)
        return len(uniqueValList)

    def isLocked(self, pos):
        return self._actv.test(pos)

    def lockBits(self):
        # Percorre todos os bits não ativos de Actv
        for i in range(self._actv.getSize()):
            if not self._actv.test(i):
                j = 1
                state = self._mem[0].test(i)
                # Verifica se os bits das valorações da memória nessa posição são todos iguais
                while j < len(self._mem) and self._mem[j].test(i) == state:
                    j += 1
                # Ativa o bit de Actv se forem todos iguais
                if j >= len(self._mem):
                    self._actv.st(i)

    def getActvCount(self):
        return self._actv.count()

    def getPrMut(self):
        return self._PrMut

    def setPrMut(self, prMut):
        self._PrMut = prMut
