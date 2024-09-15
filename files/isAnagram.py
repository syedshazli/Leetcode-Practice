#Notes
# All we need to do is check if the FREQUENCY of characters in the first string matches that of the second string
# We can do this by making 2 hashmaps (dictionaries in Python), one for string s and one for string t
# Then go through all characters in s. The 'key' is the character and the value is Hashmap.get(char, 0) +1
# Do the same for all characters in t.
# In python when we do equals equals for the two hashmaps, it will essentially check if the frequencies are the same.
# Function will return true if the frequencies in hashmaps are the same and false otherwise
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #probably another hashmap problem
        # t has to be in s
        #2 separate for loops
        # first one should loop through s, adding occurences to hashmap
        # second loop iterates through t, checking if the current letter is in s
        if len(s)!=len(t):
            return False
        
        hashmap = dict()
        hashmapT = dict()
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0)+1
        
        for i in range(len(t)):
            hashmapT[t[i]] = hashmapT.get(t[i],0)+1
            # if t[i] not in hashmap:
            #     return False
            # else:
            #     flag = True
            #     print(t[i])
        return hashmapT == hashmap
        
