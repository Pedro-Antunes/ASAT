from bitset import Bitset


class Individuo:

    def __init__(self, id, val):
        self._id = id
        self._val = val
        self._eval = None
        self._mem = []
        self._actv = Bitset()
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
        self._mem.append(x)

    def forget(self):
        self._mem = []

    def valCount(self):
        return len(self._mem)

    def uniqueValCount(self):
        valSet = set()
        for val in self._mem:
            valSet.add(val.asInt())
        return len(valSet)

    def isLocked(self, bit):
        return self._actv.test(bit)

    def lockBits(self, N):
        for i in range(N):
            if not self._actv.test(i):
                j = 1
                state = self._mem[0].test(j)
                while j < len(self._mem) and self._mem[j].test(j) == state:
                    j += 1
                if j >= len(self._mem):
                    self._actv.set(i)

    def getPrMut(self):
        return self._PrMut

    def setPrMut(self, prMut):
        self._PrMut = prMut
