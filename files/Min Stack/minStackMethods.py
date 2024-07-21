class MinStack(object):
    obj = []

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        # trying to set minimum of val and top of minstack to val
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
            #append sumn

        """
        :type val: int
        :rtype: None
        """

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
       

        

    def top(self):
        """
        :rtype: int
        """
        #the top of the stack will be the last element in an array... right?
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        #keep a running track of a value with this
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
