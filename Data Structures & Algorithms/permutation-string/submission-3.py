class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def cind(char):
            return ord(char.lower()) - ord('a') 
        
        
        if len(s1) > len(s2): return False
        
        small_counts = [0] * 26
        for c in s1: small_counts[cind(c)] += 1
        
        counts = [0] * 26
        for i in range(0, len(s1)): counts[cind(s2[i])] += 1
        if counts == small_counts: return True

        for i in range(0, len(s2) - len(s1)):
            counts[cind(s2[i])] = max(0, counts[cind(s2[i])] - 1)
            counts[cind(s2[i + len(s1)])] += 1
            print("removing:", s2[i], "adding:", s2[i + len(s1)], s2[i:i+len(s1)], counts)
            if counts == small_counts: return True
        

        return False