#Notes
# Not a terrible problem, just needed help getting started with def__init__ and intiialziing the two stacks as arrays
# The caveat or hard part of the problem comes in retrieiving the minium in O(1) time. We can do this by having another stack that keeps track of the minimum
# whenever you push, check to see if the val being pushed is less than the minimum (only if the length of the minstack exists)
#    if it is, make val equal to the end of the minStack
# outside the if, append to the minStack the val
#pop, top, annd getmin are one liners as a result of our minStack, Just remember to also pop from minstack when popping from normal stack
class MinStack(object):
 

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
