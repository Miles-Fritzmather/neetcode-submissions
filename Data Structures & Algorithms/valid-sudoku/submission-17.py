class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if (cell == "."): continue
                if (cell in seen): 
                    print("row fail", row, cell, seen)
                    return False
                else: seen.add(cell)

        # Check cols
        seen = [set() for i in range(len(board))]
        print(seen)
        for row in board:
            for j, cell in enumerate(row):
                if (cell == "."): continue
                if (cell in seen[j]): 
                    print("col fail")
                    return False
                else: seen[j].add(cell)

        # Check square
        for r in range(0, 9):
            seen = set()
            x = (r % 3) * 3
            y = (r // 3) * 3
            print("x, y", x, y)
            for i in range(0, 3):
                print("i: ", i)
                for j in range(0, 3):
                    print("j", j)
                    if board[y + i][x + j] == ".": continue
                    if (board[y + i][x + j] in seen): 
                        print("square fail", seen, board[y + i][x+j])
                        return False
                    else: 
                        print("just saw ", board[y + i][x + j])
                        seen.add(board[y + i][x + j])

        return True
            