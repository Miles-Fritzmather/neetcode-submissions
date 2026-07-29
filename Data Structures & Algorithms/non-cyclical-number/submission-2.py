class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()
        new = 0
        while new not in seen:
            seen.add(new)
            new = 0
            for d in s: new += int(d) ** 2
            if new == 1: return True
            s = str(new)
            print(str(new))
                
        return False