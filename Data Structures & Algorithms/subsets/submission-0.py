class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [[], nums]

        subsets = self.subsets(nums[1:])
        l = len(subsets)
        for i in range(l):
            subsets.append(subsets[i] + [nums[0]])
            
        return subsets