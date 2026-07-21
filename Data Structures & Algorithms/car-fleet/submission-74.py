import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], (target - position[i]) / speed[i]) for i in range(len(speed))]
        pairs.sort(key=lambda pair: -pair[0])
        
        clusters = 1
        slowest = pairs[0][1]
        for i in range(1, len(pairs)):
            time = pairs[i][1]
            
            if time > slowest: clusters += 1
            slowest = max(slowest, time)

        return clusters