#right-left +1 is the size of the window
# on each iteration add the string and its occurence 
# if the windown size - the greatest hashmap value is greater than k, remove the occurence of the character on left pointer, 
# incremenet left pointer by 1
# result = max of result and the window size
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap = {}
        left = 0
        res = 0
        
        # sliding window... while inside a for?
        #uses a hash table as well...
        #occurences of most comment letter, find the max in hashmap?
        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)

            if (right-left+1) - max(hashmap.values())> k:
                hashmap[s[left]] -= 1
                left+=1
               
            
            res = max(res, right-left+1)


        return res
        
