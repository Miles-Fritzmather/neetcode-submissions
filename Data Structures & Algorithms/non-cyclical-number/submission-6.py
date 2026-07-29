class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()
        new = 0
        while new not in seen:
            seen.add(new)
            new = sum([int(d) ** 2 for d in s])
            if new == 1: return True
            s = str(new)
                
        return False