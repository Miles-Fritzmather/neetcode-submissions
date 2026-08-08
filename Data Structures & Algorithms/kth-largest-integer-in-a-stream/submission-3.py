import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        print("adding: ", val)
        if (len(self.nums) == self.k):
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
            print(self.nums)
            return self.nums[0]
        else:
            heapq.heappush(self.nums, val)
            print(self.nums)
            return self.nums[0]
        
