import random


class Populacao:

    def __init__(self):
        self._elem = {}

    def add(self, individuo):
        self._elem.update({individuo.getId() : individuo})

    def replace(self, individuo):
        self._elem.update({individuo.getId() : individuo})
        
    def getIndividuo(self, idt):
        return self._elem.get(idt)

    def getAll(self):
        return list(self._elem.values())

    def getRandomOther(self, idt):
        r = random.randint(0, len(self._elem)-2)
        if r >= idt:
            r += 1
        return self._elem.get(r)