#return len(stack)==0. This is because if the 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        flag = True
        for char in range(len(s)):
            if s[char] == '(':
                stack.append(')')
            elif s[char] == '{':
                stack.append('}')
            elif s[char] == '[':
                stack.append(']')
          
            elif len(stack) == 0 or stack.pop() != s[char]:
                return False

            
  
        return len(stack)==0
            
