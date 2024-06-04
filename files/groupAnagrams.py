from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        newMap = {}
        resultList = []
        newWord = ""
       
        for word in strs:
            words = sorted(word)
            words = ''.join(words)

            if words not in newMap:

                newMap[words] = [word]
            else:
                newMap[words].append(word) 

        for val in newMap:
            #obtain value from key and put it in the list of lists
            x = newMap.get(val)
            resultList.append(x)
        
        return resultList

        
