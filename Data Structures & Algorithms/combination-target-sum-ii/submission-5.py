class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        counts = {}
        for c in candidates: counts[c] = 1 + counts.get(c, 0)
        nums = list(set(candidates))
        
        def sub(current: List[int], total: int, numIndex: int, repeat: int):
            if total == target: res.append(current.copy())
            elif total < target:
                if repeat < counts[nums[numIndex]]:
                    sub(
                        current + [nums[numIndex]], 
                        total + nums[numIndex], 
                        numIndex, 
                        repeat + 1
                    )
                if numIndex < len(nums) - 1: sub(current, total, numIndex + 1, 0)

        sub([], 0, 0, 0)
        return res