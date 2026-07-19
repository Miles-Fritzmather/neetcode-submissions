class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                best = max(best, self.waterAmt(heights, i, j))
        return best
            
        

    def waterAmt(self, heights: List[int], i: int, j: int) -> int:
        return min(heights[i], heights[j]) * (j - i)