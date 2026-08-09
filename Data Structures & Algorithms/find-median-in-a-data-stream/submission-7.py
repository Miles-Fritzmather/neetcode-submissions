import bisect

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.values, num)

    def findMedian(self) -> float:
        l = len(self.values)
        mid = l // 2
        if l % 2 == 1: return self.values[mid]
        else:          return (self.values[mid - 1] + self.values[mid]) / 2
        