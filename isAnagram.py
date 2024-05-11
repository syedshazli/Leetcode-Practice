#Notes
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        firstFrequency = {}
        secondFrequency = {}

        for char in s:
            firstFrequency[char] = firstFrequency.get(char, 0)+1

        for char in t:
            secondFrequency[char] = secondFrequency.get(char, 0) +1

           
        return firstFrequency == secondFrequency
        
        
