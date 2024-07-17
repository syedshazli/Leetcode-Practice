class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
       
        
        #created the window, slide it over
        str1 = Counter(s1)
        str2 = Counter(s2[0:len(s1)])
        #ex 0:2, now if the frequencies are equal then return true
            #but if not, keep sliding the window
        #hashtable, add onto a certain key if it's still a valid permutation
        # if not, move pointers
        #1,len(s2)-len(s1)+1
        #len(s2)-1
        for i in range(len(s2)-len(s1)):
            if str1 == str2:
                return True
            else:
             

                str2[s2[i]] = str2.get(s2[i], 0)-1
                if str2[s2[i]] == 0:
                    str2.pop(s2[i])

                str2[s2[len(s1)+i]] = 1 + str2.get(s2[len(s1)+i],0)
        
        return str1 == str2
     
    
