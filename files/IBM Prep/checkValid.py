class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected_set = set(i for i in range(1, n+1))
        print(expected_set)
        for r in range(len(matrix)):
            if set(matrix[r]) != expected_set:
                return False
            if set(matrix[c][r] for c in range(len(matrix[r])))!=expected_set:
                return False
        return True
