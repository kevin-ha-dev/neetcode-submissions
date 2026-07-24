class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0, 9):
            seen: set[str] = set()
            for i in range(0, 9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for column in range(0, 9):
            seen: set[str] = set()
            for i in range(9):
                if board[i][column] == ".":
                    continue
                if board[i][column] in seen:
                    return False
                seen.add(board[i][column])
        
        for square in range(0, 9):
            seen: set[str] = set()
            start_row: int = (square // 3) * 3
            start_column: int = (square % 3) * 3

            for i in range(0,3):
                for j in range(0,3):
                    if board[start_row + i][start_column + j] == ".":
                        continue
                    if board[start_row + i][start_column + j] in seen:
                        return False
                    seen.add(board[start_row + i][start_column + j])
        return True

