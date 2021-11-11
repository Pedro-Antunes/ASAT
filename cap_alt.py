from evento import Evento


class CAP:

    def __init__(self):
        self._eventList = []

    def add(self, evt: Evento):
        left = 0
        right = len(self._eventList)
        while left < right:
            mid = (left + right) // 2
            if evt.getTime() > self._eventList[mid].getTime():
                right = mid
            else:
                left = mid + 1
        self._eventList.insert(left, evt)

    def next(self):
        return self._eventList[-1]

    def remove(self):
        self._eventList.pop()
