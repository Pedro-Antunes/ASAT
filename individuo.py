from bitset import Bitset
from valoracao import Valoracao


class Individuo:

    def __init__(self, id):
        self._id = id
        self._val = Valoracao()
        self._mem = []
        self._actv = Bitset()
        self._PrMut = 0.5
        self._coef = None

    def setValoracao(self, val):
        self._val = val

    def getId(self):
        return self._id
    
    def getValoracao(self):
        return self._val

    def getPrMut(self):
        return self._PrMut

    def memorize(self, x):
        self._mem.append(x)

    def valCount(self):
        return len(self._mem)

    def uniqueValCount(self):
        pass

    def isLocked(self, bit):
        return self._actv.get(bit)

    def setCoef(self, coef):
        self._coef = coef

    def getCoef(self):
        return self._coef
