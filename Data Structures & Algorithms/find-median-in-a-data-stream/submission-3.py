import bisect

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.values, num)

    def findMedian(self) -> float:
        l = len(self.values)
        if l % 2 == 1:
            return self.values[l // 2]
        else:
            return (self.values[l // 2 - 1] + self.values[l // 2]) / 2
        