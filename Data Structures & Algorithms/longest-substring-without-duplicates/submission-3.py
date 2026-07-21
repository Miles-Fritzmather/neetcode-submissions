class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        l = 0
        r = 1
        best = 1
        while r < len(s):
            print(l, r, s[l:r], best)
            if (ind := s[l:r].find(s[r])) != -1:
                l += ind + 1
                print("found an issue: ", ind + 1, s[l:r])
            r += 1
            best = max(best, r-l)
    
        return best