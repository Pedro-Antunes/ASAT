class Evento:

    def __init__(self, kind, time, target):
        self._info = (kind, time, target)

    def getKind(self):
        return self._info[0]

    def getTime(self):
        return self._info[1]

    def getTarget(self):
        return self._info[2]
