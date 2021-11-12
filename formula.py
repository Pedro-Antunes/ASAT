class Formula:

    def __init__(self, path):
        self._varCount = 0
        self._clauseCount = 0
        self._clauses = []
        for line in open(path, "r"):
            if not line.startswith("c") and len(line) > 2:
                args = line.split()
                if args[0] == "p":
                    self._varCount = int(args[2])
                    self._clauseCount = int(args[3])
                else:
                    lineVars = []
                    for literal in args:
                        if literal != "0":
                            lineVars.append(int(literal))
                    self._clauses.append(lineVars)

    def getVarCount(self):
        return self._varCount

    def getClauseCount(self):
        return self._clauseCount

    def evaluate(self, valoracao):
        satisfy = 0
        for cl in self._clauses:
            i = 0
            while i < len(cl) and (valoracao.test(abs(cl[i]) - 1) != (cl[i] > 0)):
                i += 1
            if i < len(cl):
                satisfy += 1
        return satisfy
