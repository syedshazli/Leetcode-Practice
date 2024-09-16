class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we already know what an anagram is. It's just the occurences of strings in a hasmap
        # we also know how to find out if two strings are anagrams as well
        #could also sort everything in list
      
        resArr = []

        hashmap = {}
        # at the end, while loop over hashmap 
        #my issue is finding the proper way to actually append this to a list.
        # We find the two are anagrams, and then what? While loop?
        sortList = []
        #sort each word, make it the key and the value is the actual word
        for i in range(len(strs)):
            sort = list(strs[i])
            sort.sort()
            sort = "".join(sort)
            if sort not in hashmap:
                sortList.append(sort)
                hashmap[sort] =  [strs[i]] 
            else:
                hashmap[sort].append(strs[i])
        # print(hashmap)
        # print(sortList)
        for i in range(len(sortList)):
            printed = hashmap[sortList[i]]
            resArr.append(printed)


        return resArr
