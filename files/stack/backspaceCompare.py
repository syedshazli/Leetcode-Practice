class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # return a boolean, true or false
        # we have two separate arrays, do not have to be same size
        # can do a forward traversal of array, if the current element is #, then we pop
        # otherwise, we add to array
        # check if the two respective stacks are equal
        # s = ab#c, t = ad#c
        # stack is empty
        # traverse thru s
        # add a to stack
        # add b to stack
        # we have a '#', so pop b from stack
        # add c to stack
        stackS = []
        stackT = []

        for i in range(len(s)):
            if len(stackS) == 0 and s[i] == '#':
                continue
            elif s[i] == '#' and stackS:    
                stackS.pop()
            else:
                stackS.append(s[i])
        
        for j in range(len(t)):
            if len(stackT) == 0 and t[j] == '#':
                continue
            elif t[j] == '#' and stackT:
                stackT.pop()
            else:
                stackT.append(t[j])
             

        # print(stackT)
        # print(stackS)
        return stackT == stackS
        
