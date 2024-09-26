class Solution:
    def isPalindrome(self, s: str) -> bool:
        # figure out how to get all upercase leters into lowercase
        # remove punctuation
        # also remove spaces (make it a list of chars and do "".join)
        
        #once that is done. 2 pointers
        # one starts at the front of s and the other at the back
        # if s[i] and s[j] are not equal, return false
        # else, i +=1 and j -=1
        s = s.lower()
        newString = []
        notAllowed = set(string.punctuation)
        for i in range(len(s)):
            if s[i] not in notAllowed and s[i] != " ":
                newString.append(s[i])
        newString = "".join(newString)
        i = 0
        j = len(newString)-1
        while i <= j:
            if newString[i] != newString[j]:
                return False
            i +=1
            j-=1
        
      #  print(s)
        return True
        
