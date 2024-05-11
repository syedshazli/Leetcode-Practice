#Notes
# All we need to do is check if the FREQUENCY of characters in the first string matches that of the second string
# We can do this by making 2 hashmaps (dictionaries in Python), one for string s and one for string t
# Then go through all characters in s. The 'key' is the character and the value is Hashmap.get(char, 0) +1
# Do the same for all characters in t.
# In python when we do equals equals for the two hashmaps, it will essentially check if the frequencies are the same.
# Function will return true if the frequencies in hashmaps are the same and false otherwise
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
        
        
