
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        listS1 = list(s1)
        listS1.sort()

        if len(s2)<len(s1):
            return False
            
        while i + len(s1)<=len(s2):
            listS2 = list(s2[i:i+len(s1)])
            listS2.sort()

            if listS2 == listS1:
                return True
            i+=1
        return False
        
