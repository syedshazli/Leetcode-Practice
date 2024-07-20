#return len(stack)==0. This is because if there is only one opening parenthesis (ex: '('  ) then the stack appends the closing ')'
#the length of the string s is only 1 so if we returned true outside the loop, this would be a problem because we can't check the next character to validate that it;s in the string
# the reason len(stack) == 0 should return true is that the stack length being 0 outside the for loop means everything checks out. Every opening found a closing partner
# if we found stack == 0 inside the for loop, this means we did not append a opening tag at all, and instead the current cgaracter is a closing tag without a opening one
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
            
