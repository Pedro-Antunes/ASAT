class CAP:

    def __init__(self):
        self._eventMap = {}

    def add(self, evento):
        if evento.getKind() not in self._eventMap:
            self._eventMap[evento.getKind()] = []
        kindList = self._eventMap[evento.getKind()]
        left = 0
        right = len(kindList)
        while left < right:
            mid = (left + right) // 2
            if evento.getTime() > kindList[mid].getTime():
                right = mid
            else:
                left = mid + 1
        kindList.insert(left, evento)

    def next(self):
        assert len(self._eventMap) > 0
        nextEvent = None
        for lst in self._eventMap.values():
            if nextEvent is None:
                nextEvent = lst[-1]
            elif lst[-1].getTime() < nextEvent.getTime():
                nextEvent = lst[-1]
        return nextEvent

    def remove(self):
        nextEvent = self.next()
        self._eventMap[nextEvent.getKind()].pop()
        if self._eventMap[nextEvent.getKind()] == []:
            self._eventMap.pop(nextEvent.getKind())
