# TIME: 6 minutes, 42 seconds
# the input array is sorted.
        # find 2 numbers that add up to target. Must be at different indices
        # return the 2 indices (1 indexed) as an array
        # CANNOT USE SAME ELEMENT TWICE
        #

        # in binary search, we look for a number by having left and right bounds
        # here, we can say while left<=right
        #   if nums[left] + nums[right] >target:
            #right-=1
        # elif nums[left] + nums[right]<target:
        #   left +=1
        #else:
        # resArr.append(left+1)
        #resArr.append(right+1)
        #break
        #notice how while loop is not left <=right. or else the two indices will be equal
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        resArr = []
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right -=1
            elif numbers[left]+numbers[right]<target:
                left +=1
            else:
                resArr.append(left+1)
                resArr.append(right+1)
                return resArr
        return resArr
