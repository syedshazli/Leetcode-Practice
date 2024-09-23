class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashmap for each row, column, and 3x3?
        # bc we are not checking for all numbers (1-9), we're just checking for duplicates
        # reason being is bc if we find a duplicate in any row, column, or 3x3:
            #then we know it's invalid
            #the issue is we don't want to make 27 hashmaps (1 for each 3x3, row, col)
            # or do we?
        #create a hashmap on each iteration, if it's count ever exceeds 1 we return false
        #I just need to figure out how to find 3x3.. it involves // and %
        #divide by 3?
        #row 8, column 8
        # 8/3 +8/3
        #determine subgrid using this formula
            #index = ((row / 3) * 3 + (col / 3))
            #note the subgrids are 0 indexed
        
        print((5//3)*3 + (6//3))
        #so is there any way to determine the boxes and just append based on this
        
        for r in range(len(board)):
            row = []
            col = []
            box = []
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    row.append(board[r][c])
                
                if board[c][r] != ".":
                    if board[c][r] in col:
                        return False
                    col.append(board[c][r])



                box_row = 3* (r//3)
                box_col = 3*(r%3)
                if board[box_row+c//3][box_col+c%3]!= ".":
                    if board[box_row+c//3][box_col+c%3] in box:
                        return False
                    box.append(board[box_row+c//3][box_col+c%3])
        return True
