import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [(position[i], speed[i], (target - position[i]) / speed[i]) for i in range(len(speed))]
        comb.sort(key=lambda a: a[0])
        
        clusters = 1
        slowest = comb[-1][2]
        for i in range(len(comb) - 2, -1, -1):
            if comb[i][2] > slowest: clusters += 1
            slowest = max(slowest, comb[i][2])

        return clusters