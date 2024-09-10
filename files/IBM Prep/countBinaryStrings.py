class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # not empty
        # binary string - a string of 0's and 1's
        #returning an integer
        #once we get by what it actually means to have equal # of consecutive 1's and 0's, the problem is easy
        
        #equal number of consecutive 1's and 0's. THIS DOESNT MEAN YOU HAVE TO HAVE SAME # OF 1's and 0's IN ALL SUBSTRINGS!!!!
        # so for 0011, it's looking. How many 0's do we have, and is it equal to the amount of 1's we have. 
        count = 0
        preLen = 0
        currentLen = 1

        # people are saying it requires multiple iterations, so separate forr loops?

        for i in range(1, len(s)):
            #do something
            # two pointers. Increment right pointer by one and left ptr by one if we find a valid match. 
            #If we dont.. then increment right pointer by one only?
            if s[i] == s[i-1]:
                currentLen+=1
            else:
                preLen = currentLen
                currentLen = 1
            
            if preLen>=currentLen:
                count+=1
        return count
