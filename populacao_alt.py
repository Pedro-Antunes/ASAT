import random


class Populacao:

    def __init__(self):
        self._elem = {}

    def add(self, individuo):
        self._elem.update({individuo.getId() : individuo})

    def replace(self, individuo):
        self._elem.update({individuo.getId() : individuo})
        
    def getIndividuo(self, id):
        return self._elem.get(id)

    def getAll(self):
        return list(self._elem.values())

    def getRandomOther(self, id):
        r = random.randint(0, len(self._elem)-2)
        if r >= id:
            r += 1
        return self._elem.get(r)