class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap = dict()
        # sliding window... while inside a for?
        #uses a hash table as well...
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1 #correctly populate

            
            left = i
            right = i+k
            print(hashmap)
        return 0
        
