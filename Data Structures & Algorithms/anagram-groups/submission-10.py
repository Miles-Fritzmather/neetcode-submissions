class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        masterCounts = []
        for s in strs:
            counts = {}
            for c in s:
                counts[c] = counts.get(c, 0) + 1
            
            index = self.foo(masterCounts, counts)

            if index != -1: groups[index].append(s)
            else: 
                groups.append([s])
                masterCounts.append(counts)
        return groups

    def foo(self, masterCounts, counts) -> int:
        for i, m in enumerate(masterCounts):
            if m == counts: return i
        return -1