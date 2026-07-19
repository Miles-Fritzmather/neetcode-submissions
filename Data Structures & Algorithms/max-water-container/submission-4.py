class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        i = 0
        j = len(heights) - 1
        while j > 0 and i < len(heights):
            if heights[i] < heights[j]:
                best = max(best, heights[i] * (j - i))
                i += 1
            else:
                best = max(best, heights[j] * (j - i))
                j -= 1
            
                
        return best