class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper = len(matrix)
        lower = 0
        row = 0

        # Find row
        while lower < upper:
            i = (lower + upper) // 2
            if target < matrix[i][0]:
                upper = i - 1
            elif target > matrix[i][0]:
                if target > matrix[i][-1]:
                    lower = i + 1
                elif target < matrix[i][-1]:
                    row = i
                    break
                else: return True
            else:
                return True

        lower = 0
        upper = len(matrix[row]) - 1

        #Find col
        while lower <= upper:
            i = (lower + upper) // 2
            if target < matrix[row][i]:
                upper = i - 1
            elif target > matrix[row][i]:
                lower = i + 1
            else: return True
        
        return False