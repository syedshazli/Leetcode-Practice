class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = set()

        temp = 0
        count = 0

        for i in range(len(s)):
            if s[i] not in d:
                d.add(s[i])
                temp += 1

            else:
                d.remove(s[i])
                temp = 1

            if temp > count:
                count = temp

                                
        return count
            
