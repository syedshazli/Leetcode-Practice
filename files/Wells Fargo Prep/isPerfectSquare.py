class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if n is even, n^2 is even
        # ex/ 35 is odd so 35 /3 is not an integer, ao false
        # 34 is even. 34/2 is not even so false
        # 66 is even. 66 dvided by 2 is odd
        low = 0
        high = num
        while low<= high:
            middle = (low+high)//2
            if middle*middle>num:
                high = middle-1
            elif middle*middle <num:
                low = middle+1
            else:
                return True
        return False
        
