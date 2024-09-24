class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = collections.defaultdict(set) # key = (r//3, c//3
        for r in range(len(board)):
            row = []
            col = []
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    row.append(board[r][c])

                if board[c][r] != ".":
                    if board[c][r] in col:
                        return False
                    col.append(board[c][r])

                if board[r][c] != ".":
                    if board[r][c] in box[r//3, c//3]:
                        return False
                    box[r//3, c//3].add(board[r][c])


        return True
