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
        
