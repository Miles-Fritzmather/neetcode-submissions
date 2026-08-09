import bisect

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        self.insert(num)

    def insert(self, num: int) -> None:
        l, r = 0, len(self.values)
        while l < r:
            p = (l + r) // 2
            if num < self.values[p]:   r = p
            elif num > self.values[p]: l = p + 1
            else:                      l = r = p
        self.values.insert(l, num)



    def findMedian(self) -> float:
        l = len(self.values)
        mid = l // 2
        if l % 2 == 1: return self.values[mid]
        else:          return (self.values[mid - 1] + self.values[mid]) / 2
        