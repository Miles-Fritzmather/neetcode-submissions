class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def sub(current: List[int], total: int, numIndex: int):
            if total == target: res.append(current)
            if total < target:
                sub(current + [nums[numIndex]], total + nums[numIndex], numIndex)
                if numIndex < len(nums) - 1: sub(current, total, numIndex + 1)

        sub([], 0, 0)
        return res