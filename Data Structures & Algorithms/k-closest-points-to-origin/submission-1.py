class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            pairs.append(((x, y), distance))
        
        pairs.sort(key=lambda p: p[1])
    
        return [pair[0] for pair in pairs[0:k]]