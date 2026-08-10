class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        arr = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            if arr[i - 1] < 0: arr[i] = nums[i]
            else: arr[i] = arr[i - 1] + nums[i]
            best = max(best, arr[i])
        
        return best