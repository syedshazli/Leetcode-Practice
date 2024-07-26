
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #This relates to binary search, somehow, someway
        #what if we convert this to a normal array and do bin search
      
        colCount = len(matrix[0])
        high = matrix[len(matrix)-1][len(matrix[0])-1]
        low = matrix[0][0]
        # print(high)
        # print(low)
        lowIndex = 0
        highIndex = (len(matrix) * len(matrix[0]))-1
        # print(highIndex)
        # print(lowIndex)

        if target == matrix[0][0]:
            return True
        

      
         
        while lowIndex < highIndex:
            mid = lowIndex + (highIndex-lowIndex+1)/2
            print("mid: ", mid)
            # no. of rows = mid/c
            # no. of cols= mid%c
            print[matrix[mid/colCount][mid%colCount]]
            if matrix[mid/colCount][mid%colCount] > target:
                highIndex = mid-1
            elif matrix[mid/colCount][mid%colCount] < target:
                lowIndex = mid
            else:
                return True
        return False
            #how are we supposed to figure out the row and the column
        # print(mid)

      
        # print(len(matrix))
        # print(len(matrix[0]))
