# REDO
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0
        left = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right],0)+1

            if right-left+1 - max(hashmap.values())>k:
                hashmap[s[left]] -=1
                left+=1
            res = max(res, right-left+1)
        return res
        
        
