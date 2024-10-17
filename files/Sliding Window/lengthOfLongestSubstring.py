class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring, no repeating characters
        # sliding window
        # we need to stay in place
        # we want to make sure what's in the substring is not repeated 
        # figure out if we're in a repeating phase or if we're in a new string phase
        # if not repeating, initialise an array to use and set repeating to True
        # if we found the current character is already in our array, set repeating to False, and initalize the array to empty again. Also move left pointer up 1 and right pointer to left pointer +1 


        # for correct solution, makes sense cuz for abcdbefg, max substring is 6
        #
        maxLength = 0
        left = 0
        maxSet = set()
        for right in range(len(s)):
            while s[right] in maxSet:
                maxSet.remove(s[left])
                left+=1
            maxSet.add(s[right])
            maxLength = max(maxLength, right-left+1)
        return maxLength
