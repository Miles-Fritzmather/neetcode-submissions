import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if k > p:   return quickSelect(p + 1, r)
            elif k < p: return quickSelect(l, p - 1)
            else:       return nums[p]

        return quickSelect(0, len(nums) - 1)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heapq.heapify(nums)
    #     for i in range(len(nums) - k):
    #         heapq.heappop(nums)
    #     return nums[0]