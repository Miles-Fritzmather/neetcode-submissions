class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        l = 0
        r = 1
        best = 1
        while r < len(s):
            if (ind := s[l:r].find(s[r])) != -1: l += ind + 1
            r += 1
            best = max(best, r-l)
    
        return best