import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            diff = abs(x - y)
            if diff != 0:
                heapq.heappush(stones, -diff)
        
        return -stones[0] if len(stones) == 1 else 0
