class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        counts = {}
        for index in range(0, len(s)):
            a = s[index]
            b = t[index]
            counts[a] = counts.get(a, 0) + 1
            counts[b] = counts.get(b, 0) - 1

        for char in counts:
            print(counts[char])
            if counts[char] != 0: return False

        return True
        
        
        