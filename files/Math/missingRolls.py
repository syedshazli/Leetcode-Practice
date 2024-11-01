class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # we are missing n values and have to append to rolls so that the sum divided by len(rolls)+n divided by 
        totalRolls = len(rolls)+n # will be 7
        sumNeeded = totalRolls*mean # will be 21
        
        CurrentSumObtained = sumNeeded-sum(rolls) 
        
        # checks if it's impossible. If not, move on
        if CurrentSumObtained//n > 6:
            return []
        
        resArr = []
        numLeft = n
        while numLeft!=0:
            #simulate a sum
            if CurrentSumObtained//numLeft > 6 or CurrentSumObtained//numLeft <1:
                return []
            resArr.append(CurrentSumObtained//numLeft)
            CurrentSumObtained-= CurrentSumObtained//numLeft
            numLeft-=1
            
        return resArr

        
