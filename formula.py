from valoracao import Valoracao


class Formula:

    def __init__(self, path):
        self.varCount = 0
        self.size = 0
        self.clauses = []
        for line in open(path, "r"):
            if not line.startswith("c") and len(line) > 2:
                args = line.split()
                if args[0] == "p":
                    self.varCount = int(args[2])
                    self.size = int(args[3])
                else:
                    self.clauses.append([])
                    for literal in args:
                        if literal != "0":
                            if literal[0] == "-":
                                self.clauses[-1].append(-int(literal[1:]))
                            else:
                                self.clauses[-1].append(int(literal))

    def getVarCount(self):
        return self.varCount

    def evaluate(self, valoracao):
        satisfy = 0
        for cl in self.clauses:
            i = 0
            while i < len(cl) and (valoracao.get(abs(cl[i]) - 1) != (cl[i] > 0)):
                i += 1
            if i < len(cl):
                satisfy += 1
        return satisfy

f = Formula("uf250-01.cnf")
print(f.evaluate(Valoracao()))

