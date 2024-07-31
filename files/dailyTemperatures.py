class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #basically just asking to implement monotonic stack
        #monotonic stack means when popped things are striclty increasing or decreasing
        # if they're not, then you keep popping until they will be


        stack = [] #added index and temperature 
        #before learning about monotonic stacks, I was thinking we'd create a second array anyway
        ans =[0] * len(temperatures)

        #the stack will contain indexes only
       
        
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]: #stack[-1] indicates the top w/out popping
                stackTemp, stackIndex = stack.pop()
            
                ans[stackIndex] = index-stackIndex

            stack.append([temperature, index])
            


        return ans
