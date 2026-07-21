import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([(position[i], (target - position[i]) / speed[i]) for i in range(len(speed))], key=lambda pair: -pair[0])
        
        clusters = 1
        slowest = pairs[0][1]
        for _, time in pairs[1:]:            
            if time > slowest: clusters += 1
            slowest = max(slowest, time)

        return clusters