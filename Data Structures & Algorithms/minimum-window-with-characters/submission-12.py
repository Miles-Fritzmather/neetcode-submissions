class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        if len(t) == 1: return t if t in s else ""
        if t == s: return t
        
        tCounts = {}
        sCounts = {}
        for i in range(0, len(t)): 
            tCounts[t[i]] = 1 + tCounts.get(t[i], 0)
            sCounts[t[i]] = 0
        t = set(t)

        left, right = 0, 1
        total = 0
        if s[0] in t:
            sCounts[s[0]] += 1
            if sCounts[s[0]] == tCounts[s[0]]:
                total += 1
        best = None
        while left < len(s) - 1:
            if total < len(t):
                if right >= len(s): break
                if s[right] in sCounts:
                    sCounts[s[right]] += 1
                    if sCounts[s[right]] == tCounts[s[right]]:
                        # print("adding", s[right])
                        total += 1
                right += 1
            else:
                if s[left] in sCounts:
                    if sCounts[s[left]] == 0: continue
                    sCounts[s[left]] -= 1
                    if sCounts[s[left]] < tCounts[s[left]]:
                        # print("losing", s[left])
                        total -= 1
                left += 1
            
            if total == len(t) and (not best or best[1] - best[0] > right - left): 
                best = (left, right)
            
            # print(total, best, s[left:right], (left, right))

        return "" if best is None else s[best[0]:best[1]]
