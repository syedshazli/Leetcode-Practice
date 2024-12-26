def convertToBinary(self, n):
 
        myArr = []
        

        while n > 1:
            myArr.append(str(n%2))
            n = n//2
       

        if n ==1:
            myArr.append(str(1))
        elif n == 0:
            myArr.append(str(0))

        myArr.reverse()
        return "".join(myArr) 
        
