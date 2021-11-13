import random


class Populacao:

    def __init__(self):
        self._elem = {}

    def add(self, individuo):
        self._elem.update({individuo.getId() : individuo})

    def replace(self, idt, individuo):
        self._elem.update({idt : individuo})
        
    def getIndividuo(self, idt):
        return self._elem.get(idt)

    def getAll(self):
        return list(self._elem.values())

    def getRandomOther(self, idt):
        # Retira o individuo do dicionário, escolhe um elemento aleatório e adiciona-o de volta
        ind = self._elem.pop(idt)
        r = random.choice(self.getAll)
        self.add(ind)
        return r
