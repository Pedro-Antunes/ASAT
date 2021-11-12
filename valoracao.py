from bitset import Bitset


class Valoracao(Bitset):

    def __init__(self, N):
        super().__init__(N)

    def compare(self, val):
        if self.getSize() == val.getSize():
            isEqual = False
        else:
            i = 0
            while self.test(i) == val.test(i) and i < self.getSize():
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
