import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], (target - position[i]) / speed[i]) for i in range(len(speed))]
        pairs.sort(key=lambda pair: pair[0])
        
        clusters = 1
        slowest = pairs[-1][1]
        for i in range(len(pairs) - 2, -1, -1):
            if pairs[i][1] > slowest: clusters += 1
            slowest = max(slowest, pairs[i][1])

        print(pairs)
        pairs.sort(key=lambda pair: -pair[0])
        print(pairs)
        pairs.sort(key=lambda pair: pair[0])
        pairs.reverse()
        print(pairs)

        return clusters