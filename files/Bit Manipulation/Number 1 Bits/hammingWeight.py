def hammingWeight(self, n: int) -> int:
        myList = self.convertToBinary(n)

     
        
        num = 0
        for binary in myList:
            if binary == "1":
                num +=1
        return num
