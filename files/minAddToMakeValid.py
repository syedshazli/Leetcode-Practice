class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Can be singular element
        # can literally just count open and closed brackets.. Seems like valid parenthesis a little bit
        # if len(s) == 0: return 0
        #else
        # create a stack
        # for i in range(len(s)):
        #   if current element is closing parenthesis and top of stack is opening, pop from stack
        #   elif current element opening parenthesis, append to stack
        # else, append to stack.
        # return length of stack
        if len(s) == 0:
            return 0
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i] == ')' and len(stack)!= 0 and stack[-1] == '(':
                print("here")
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
        
