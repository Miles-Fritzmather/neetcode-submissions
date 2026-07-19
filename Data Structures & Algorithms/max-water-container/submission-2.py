class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                best = max(best, min(heights[i], heights[j]) * (j - i))
        return best