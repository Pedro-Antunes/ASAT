class Evento:

    def __init__(self, kind, time, target):
        self._kind = kind
        self._time = time
        self._target = target

    def getKind(self):
        return self._kind

    def getTime(self):
        return self._time

    def getTarget(self):
        return self._target
