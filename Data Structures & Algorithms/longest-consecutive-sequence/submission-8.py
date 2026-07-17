class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        hashed = set()
        for n in nums:
            hashed.add(n)
            if n - 1 not in nums:
                starts[n] = 0
        
        print(starts)
        for s in starts:
            i = s
            while i in hashed:
                starts[s] += 1
                i += 1
        
        print(starts)
        best = 0
        for s in starts:
            best = max(best, starts[s])
        
        return best
            
            

        
            