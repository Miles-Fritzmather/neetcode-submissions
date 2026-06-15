class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if (cell == "."): continue
                elif (cell in seen): return False
                else: seen.add(cell)

        # Check cols
        seen = [set() for i in range(len(board))]
        for row in board:
            for j, cell in enumerate(row):
                if (cell == "."): continue
                elif (cell in seen[j]):  return False
                else: seen[j].add(cell)

        # Check square
        for r in range(0, 9):
            seen = set()
            x = (r % 3) * 3
            y = (r // 3) * 3
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[y + i][x + j] == ".": continue
                    elif (board[y + i][x + j] in seen):  return False
                    else: seen.add(board[y + i][x + j])

        return True
            