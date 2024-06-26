class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            if((right-left)* min(height[right], height[left])) > result:
                result = (right-left)* min(height[right], height[left])
                
            if height[left] < height[right]:
                left +=1
            
            elif height[left] > height[right]:
                right-=1

            else:
                left+=1
                right-=1
              
              
    

        return result
        
