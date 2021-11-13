import random
from bitset import Bitset


class Individuo:

    def __init__(self, idt, valoracao):
        self._info = {
            "id" : idt, 
            "val" : valoracao, 
            "eval" : None, 
            "mem" : [], 
            "actv" : Bitset(valoracao.getSize()), 
            "PrMut": 0.5
        }

    def getId(self):
        return self._info.get("id")

    def getValoracao(self):
        return self._info.get("val")

    def setValoracao(self, valoracao):
        self._info.update({"val" : valoracao})
    
    def getEval(self):
        return self._info.get("eval")

    def setEval(self, eval):
        self._info.update({"eval" : eval})

    def memorize(self, valoracao):
        self._info.get("mem").append(valoracao)

    def getRandomMemVal(self):
        return random.choice(self._info.get("mem"))

    def forget(self):
        self._info.get("mem").clear()

    def valCount(self):
        return len(self._info.get("mem"))

    def uniqueValCount(self):
        uniqueValList = []
        for val in self._info.get("mem"):
            found = False
            i = 0
            while not found and i < len(uniqueValList):
                if val.compare(uniqueValList[i]):
                    found = True
                i += 1
            if not found:
                uniqueValList.append(val)
        return len(uniqueValList)

    def isLocked(self, pos):
        return self._info.get("actv").test(pos)

    def lockBits(self):
        actv = self._info.get("actv")
        mem = self._info.get("mem")
        for i in range(actv.getSize()):
            if not actv.test(i):
                j = 1
                state = mem[0].test(i)
                while j < len(mem) and mem[j].test(i) == state:
                    j += 1
                if j >= len(mem):
                    actv.st(i)

    def getActvCount(self):
        return self._info.get("actv").count()

    def getPrMut(self):
        return self._info.get("PrMut")

    def setPrMut(self, prMut):
        self._info.update({"PrMut" : prMut})
