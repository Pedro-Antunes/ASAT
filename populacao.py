import random


class Populacao:

    def __init__(self):
        self._elem = []

    def add(self, individuo):
        k = self._locate(individuo.getId())
        self._elem.insert(k, individuo)

    def replace(self, idt, individuo):
        k = self._locate(idt)
        self._elem[k] = individuo
        
    def getIndividuo(self, idt):
        return self._elem[self._locate(idt)]

    def getAll(self):
        return self._elem

    def getRandomOther(self, idt):
        # Gera um índice aleatório entre 0 e len(self._elem)-2 inclusive
        r = random.randint(0, len(self._elem)-1)
        # Salta o elemento idt
        if r >= self._locate(idt):
            r += 1
        # Retorna o elemento nesse índice, note-se que este não é necessáriamente igual ao identificador do indivíduo
        return self._elem[r]

    def _locate(self, idt):
        # Encontra (com pesquisa binária) o maior indice de um elemento de identificador menor ou igual a idt
        left = 0
        right = len(self._elem)
        while left < right:
            mid = (left + right) // 2
            if  idt > self._elem[mid].getId():
                left = mid + 1
            else:
                right = mid
        return left
