# A pretty weird problem honestly all things considered
# We combine the array of speeds and positions, and iterate through while sorting this combined array, in reverse order
# There is a sort of mathematics to it, we must append (target-p)/s for each iteration
# If the length of the stack is greater than 2 and the top item of the stack is less than or equal to the item before it, pop it from the stack, and return the length of the stack
# this works because we are popping it effectivley making those 2 cars 1 fleet. they will be considered as 1 car when comparing to the next car trying to join the fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # combinedSpeedPos = dict()
        
        combinedSpeedPos = [[p,s] for p,s in zip(position, speed)]
        
        # for i in range(len(position)):
        #     combinedSpeedPos[position[i]] = speed[i]
        
        #reverse sorted order
        for p,s in sorted(combinedSpeedPos)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        
