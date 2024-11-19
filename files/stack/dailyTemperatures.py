class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # another monotonic stack
        resArr = [0]*len(temperatures)
        stack = []
        # add indexes to the stack
        # if the index in the stack is less than current element, edit resArr[Index-stack[-1]] and pop from stack
        for i in range(len(temperatures)):
            while stack and temperatures[i]> temperatures[stack[-1]]:
                curr = stack.pop()
                resArr[curr] = i-curr
            stack.append(i)

        return resArr

        
