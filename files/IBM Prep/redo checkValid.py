# a problem to give me a refrsher on 2D arrays (especially in python)
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected_set = set(range(1, n + 1))  # Expected set of numbers {1, 2, ..., n}

        for r in range(n):
            row_set = set(matrix[r])  # Unique numbers in row r
            col_set = set(matrix[c][r] for c in range(n))  # Unique numbers in column r

            # Check if the row and column both contain exactly the numbers 1 to n
            if row_set != expected_set or col_set != expected_set:
                return False

        return True
