class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLUMNS: int = len(matrix[0])

        left: int = 0
        right: int = ROWS * COLUMNS - 1

        while left <= right:
            middle: int = (left + right) // 2
            row: int = middle // COLUMNS
            column: int = middle % COLUMNS
            if matrix[row][column] < target:
                left = middle + 1
            elif matrix[row][column] > target:
                right = middle - 1
            else:
                return True
        return False