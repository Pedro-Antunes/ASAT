from bitset import Bitset


class Valoracao(Bitset):

    def compare(self, valoracao):
        if self.getSize() != valoracao.getSize():
            isEqual = False
        else:
            i = 0
            while i < self.getSize() and self.test(i) == valoracao.test(i):
                i += 1
            if i != self.getSize():
                isEqual = False
            else:
                isEqual = True
        return isEqual

    def display(self):
        s = ""
        for i in range(self.getSize()):
            if self.test(i):
                s += "1"
            else:
                s += "0"
        return s
