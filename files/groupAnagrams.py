#Notes

#This took some time but I sat down with the problem and did it. Needed to surf the web to find some python dictionary methods as well
#For each word, I sorted the word, and then made the array of char's a word again by using join
#if the word wasnt in the map, we added it, with the key being the sorted word and value being the actual word
#Else, we appended the value of the sorted word to add the current word
#Then we went through the hashamp and appended to a resultant list for each value in the map
#Returned the list of lists
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

        
