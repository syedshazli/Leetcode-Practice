class Solution:
    def trap(self, height: List[int]) -> int:
        # a little bit of a pattern. When we trap the water, it means the left and right side are >= current reading
        # want the minimum of these 2
        # if value of middle pointer is less than value of right... right +=1
        num = 0
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax = max(leftMax, height[left])
                num += leftMax-height[left]
            else:
                right-=1
                rightMax = max(rightMax, height[right])
                num += rightMax - height[right]

            #do something
        return num
        
