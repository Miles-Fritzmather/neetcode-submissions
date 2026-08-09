import bisect

class MedianFinder:

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.values, num)
        # self.insert(num)

    def insert(self, num: int) -> None:
        l, r = 0, len(self.values)
        while l < r:
            p = (l + r ) // 2
            if num < nums[p]: r = p - 1
            elif num > nums[p]: l = p + 1
            else: 
                nums.insert(num, p)
                break



    def findMedian(self) -> float:
        l = len(self.values)
        mid = l // 2
        if l % 2 == 1: return self.values[mid]
        else:          return (self.values[mid - 1] + self.values[mid]) / 2
        