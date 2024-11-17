class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        stack = []
        length = 0
        for i in range(len(arr)-1,-1,-1):
            if stack and stack[-1]<arr[i]:
                length+=1
                stack.pop()
            else:
                length = 0
            
            stack.append(arr[i])
        return length

        # intuition: Once we find an element on the right that is less than the element on the left, keep incrementing the right pointer until the element on the right is not g
        # case [1, 2, 3, 2, 1, 4, 2] requires us to purge [2,1,4,2]

        # let's make it a monotonic Stack, strictly increasing. increase a count anytime we have to pop


