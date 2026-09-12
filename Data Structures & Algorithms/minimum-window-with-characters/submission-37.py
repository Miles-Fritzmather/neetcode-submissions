class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

# --------------------------------------------------

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        
        tCounts = {}
        sCounts = {}
        for i in range(0, len(t)): 
            tCounts[t[i]] = 1 + tCounts.get(t[i], 0)
            sCounts[t[i]] = 0
        t = set(t)

        left, right = 0, 1
        total = 0
        best = None
        if s[0] in t:
            sCounts[s[0]] = 1
            if  tCounts[s[0]] == 1: 
                total += 1
                if total == len(t): best = (left, right)

        while left < len(s) - 1:
            if total == len(t) and (not best or best[1] - best[0] > right - left): 
                best = (left, right)

            if total < len(t):
                if right >= len(s): break
                if s[right] in sCounts:
                    sCounts[s[right]] += 1
                    if sCounts[s[right]] == tCounts[s[right]]: total += 1
                right += 1
            else:
                if s[left] in sCounts:
                    if sCounts[s[left]] == 0: continue
                    sCounts[s[left]] -= 1
                    if sCounts[s[left]] < tCounts[s[left]]: total -= 1
                left += 1
            

        if total == len(t) and (not best or best[1] - best[0] > right - left): 
            best = (left, right)
        return "" if best is None else s[best[0]:best[1]]