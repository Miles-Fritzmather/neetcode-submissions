import bisect

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        # bisect.insort(self.values, num)
        self.insert(num)
        # print(self.values)

    def insert(self, num: int) -> None:
        l, r = 0, len(self.values)
        while l < r:
            p = (l + r) // 2
            if num < self.values[p]:   r = p
            elif num > self.values[p]: l = p + 1
            else:
                self.values.insert(p, num)
                return
        # print("found the location to insert @", l)
        self.values.insert(l, num)



    def findMedian(self) -> float:
        l = len(self.values)
        mid = l // 2
        if l % 2 == 1: return self.values[mid]
        else:          return (self.values[mid - 1] + self.values[mid]) / 2
        