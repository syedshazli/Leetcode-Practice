
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # what you want to do is keep a running sum of the current area
        # notice how you are allowed to have one container > than the other
        # so it has to be the minimum of the two ends.
        # calculate current area as min(height[i],height[j])*(j-1)

        # this means get the minimum of the current pointer. This is your height. j-i is assuming j will be ahead of i, and the difference is what you multiply
        # check if the area calculated by this is greater than the current max area. If it is, great, move j pointer over 1. if it isn't, move i pointer over 1
        # example. height = [1,8,6,2,5,4,8,3,7]. Output = 49
        # i = 0. j = 1. maxArea = 0;
        # while j<len(nums), currentArea = (1*1). 
        # 1 > 0, set maxArea to 1. j = 2
        # i = 0, j = 2. maxArea = 1. CurrentArea = min(1, 6)*(2)
        left = 0
        right = len(height)-1
        maxArea = 0
        while left<=right:
            currentArea = min(height[left],height[right])*(right-left)
            maxArea = max(maxArea, currentArea)

            if height[left]<height[right]:
                left +=1
            elif height[left]>height[right]:
                right -=1
            else:
                left+=1
                right -=1

        return maxArea
