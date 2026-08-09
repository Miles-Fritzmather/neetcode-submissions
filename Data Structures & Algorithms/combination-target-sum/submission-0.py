class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = []
        
        def sub(current: List[int], numIndex: int):
            s = sum(current)
            if s == target: total.append(current)
            if s < target:
                sub(current + [nums[numIndex]], numIndex)
                if numIndex < len(nums) - 1: 
                    sub(current, numIndex + 1)
        sub([], 0)
        return total