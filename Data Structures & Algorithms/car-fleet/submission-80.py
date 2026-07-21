import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sorted by position, descending
        times = sorted(
            [(position[i], (target - position[i]) / speed[i]) for i in range(len(speed))], key=lambda pair: -pair[0]
        )
        
        clusters = 1
        slowest = times[0][1]
        for _, time in times[1:]:            
            if time > slowest: clusters += 1
            slowest = max(slowest, time)

        return clusters