class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        hashed = set()
        for n in nums:
            hashed.add(n)
            if n - 1 not in nums:
                starts[n] = 0

        if len(starts) == 0: return 0
        
        for s in starts:
            i = s
            while i in hashed:
                starts[s] += 1
                i += 1
        
        best_l = list(starts.values())
        test =  [1, 3, 5, 6 , 0]
        print(max(test))
        print(max(best_l))
        best = max(best_l)
        
        # best = 0
        # for s in starts:
        #     best = max(best, starts[s])
        
        return best
            
            

        
            