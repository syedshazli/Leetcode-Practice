#Notes
# A pretty good problem. Initial appraoch was to try and flatten 2D array into 1D but didnt know how to do in under O(n^2)
# Instead, I thought myabe finding the actual low and high values would be important, but it wasn't. This helped me find the rows, columns, and max/min vals though
# The way you calculate middle in this problem is different. MIddle here equals 1 more than our normal middle calculation
# The crux of the problem was then figuring out how to access the rows and columns based on our middle values. We did this through here: [mid/colCount][mid%colCount]
# Reminder to not add one to the middle count if your bounds are too low. SUbtract 1 from high count if bounds are too low
# Good improvement
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
            mid = (lowIndex + (highIndex-lowIndex+1)/2)+1
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
