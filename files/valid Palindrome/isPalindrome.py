class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #first convert everything to lowercase
        #try not to abuse python methods, and actually use 2 pointers
        s = s.lower() #removes lowercase
        exclude = set(string.punctuation)
        s = ''.join(ch for ch in s if ch not in exclude)
        s = s.replace(" ","" )
        newString = ""
        for i in range(len(s)-1, -1, -1):
            newString += s[i]

        if newString == s:
            return True
        return False
        
