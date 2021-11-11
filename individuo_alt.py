from valoracao import Valoracao
from bitset import Bitset


class Individuo:

    def __init__(self, id, val):
        self._id = id
        self._val = val
        self._eval = None

        self._mem = {}
        self._memCount = 0

        self._actv = Bitset(val.getSize())
        self._PrMut = 0.5

    def getId(self):
        return self._id

    def getValoracao(self):
        return self._val

    def setValoracao(self, val):
        self._val = val

    def setEval(self, eval):
        self._eval = eval

    def getEval(self):
        return self._eval

    def memorize(self, x):
        if x in self._mem:
            self._mem.update({x : self._mem.get(x) + 1})
        else:
            self._mem.update({x : 1})
        self._memCount += 1   

    def forget(self):
        self._mem = {}
        self._memCount = 0

    def valCount(self):
        return self._memCount

    def uniqueValCount(self):
        return len(self._mem)

    def isLocked(self, bit):
        return self._actv.test(bit)

    def getActvCount(self):
        return self._actv.count()

    def lockBits(self, N):
        for i in range(N):
            if not self._actv.test(i):
                j = 1
                state = list(self._mem.keys())[0].test(i)
                while j < len(self._mem) and list(self._mem.keys())[j].test(i) == state:
                    j += 1
                if j >= len(self._mem):
                    self._actv.set(i)

    def getPrMut(self):
        return self._PrMut

    def setPrMut(self, prMut):
        self._PrMut = prMut
