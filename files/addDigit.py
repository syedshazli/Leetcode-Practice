
class Solution:
    def addDigits(self, num: int) -> int:
        #while loop that calls add on each iter
        def add(num):
            count = 0
            for x in str(num):
                count += int(x)
            return count

        
        while len(str(num))>1:
            num =add(num)
        return num
        
            #do a function that will add the two digits within a for loop
        
