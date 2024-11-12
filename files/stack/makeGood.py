class Solution:
    def makeGood(self, s: str) -> str:
        # no two adjacent characters
        # adjacent in this case means the same letter twice but one in upper and other in lower
        # must choose 2 adjacent characters and remove them
        # we know popping takes out the last element as well, so we just have to pop twice anytime the circumstance is filled
        # while i is less than length of s
        #   check if the current character and the character before it are same 
        # if so, pop from stack twice, decrease i twice
        # otherwise, add to stack, increase i by 1

        # example:
        # leEeetcode
        # i = 0, len(s) -1= 9
        # s[i] = l, s[i+1] = e
        # stack is empty
        # check is s[i] == s[i+1]
        # append l and e to stack, increment i by 2
        # i = 2
        # check if next element is equal to element at end of stack.. if it is, pop both
        i = 0
        stack = []
        # for each character, check if it forms a bad pair with last character appended, if so, remove last character from result
        for i in range(len(s)):
            if stack and stack[-1].lower() == s[i].lower() and s[i]!= stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
