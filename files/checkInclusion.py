
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        if s2 == s1:
            return True
        
        #created the window, slide it over
        str1 = Counter(s1)
        str2 = Counter(s2[0:len(s1)])
        #ex 0:2, now if the frequencies are equal then return true
            #but if not, keep sliding the window
        #hashtable, add onto a certain key if it's still a valid permutation
        # if not, move pointers
        for i in range(len(s2)-1):
            if str1 == str2:
                return True
            else:
                # str2[s2[i:len(s1)+i]] = str2[s2[i:len(s1)+i]]-1
                # # hashmap[s[right]] = 1 + hashmap.get(s[right],0)
                # str2[s2[i+1:len(s1)+i+1]] = 1 + str2.get(s2[i+1:len(s1)+i+1],0)
                # print(str1)
                # print(str2)
                str2 = Counter(s2[i:len(s1)+i])

    
