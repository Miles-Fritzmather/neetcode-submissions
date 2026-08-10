class Solution:
    def jump(self, nums: List[int]) -> int:
        canReach = 0
        farthest = 0
        jumps    = 0
        i = 0
        while i < len(nums) and canReach < len(nums) - 1:
            dist = i + nums[i]
            farthest = max(farthest, dist)
            if i == canReach:
                print("new limit", canReach, farthest, jumps, i)
                canReach = farthest
                jumps += 1
            i += 1
        
        return jumps