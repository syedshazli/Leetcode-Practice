class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = set()

        temp = 0
        count = 0
        left = 0
        

        #maybe use while loop inside for loop?
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left +=1           

            d.add(s[right])
            temp += 1
            
            count = max(temp, right-left+1)

                                
        return count
            
