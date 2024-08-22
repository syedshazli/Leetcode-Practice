# each number is sum of two number directly above
# how to calculate numbers directly above?

#given the number of rows we should return of the triangle
# return type is a array of arrays (2D), with 5 rows 

#each number on the end of each row is a 1.
# two for loops....

#if row and col number are same, or col number is 0 their result is 1 
# otherwise
class Solution(object):
    def generate(self, numRows):

        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        gen = []
        for k in range(numRows):
            gen.append([0]*(k+1))
        for i in range(numRows):
            for j in range(i+1):
                if i == j or j == 0:
                    gen[i][j] =1
                else:
                    gen[i][j] = gen[i-1][j-1]+gen[i-1][j]

        return gen
