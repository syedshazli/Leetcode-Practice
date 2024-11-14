class Solution:
    def arrangeCoins(self, n: int) -> int:
        # probably want to have a coin array somewhere to store previous results
        newN = n
        numRows = 0
        for i in range(1,n+1):
            newN-=i
            if newN <0:
                return numRows
            numRows+=1
        return numRows

            
        
