class Solution:
    def jump(self, nums: List[int]) -> int:
        canReach = farthest = jumps = i = 0
        while i < len(nums) and farthest < len(nums) - 1:
            farthest = max(farthest, i + nums[i])
            if i == canReach:
                canReach = farthest
                jumps += 1
            i += 1
        
        return jumps if farthest == canReach else jumps + 1