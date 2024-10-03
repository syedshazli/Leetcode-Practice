class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resArr = []
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            #left = i+1
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                currentSum = nums[i] + nums[right] +nums[left]

                if currentSum > 0:
                    right -=1

                elif currentSum < 0:
                    left +=1

                else:
                    resArr.append([nums[i], nums[right], nums[left]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
                    right -=1
        return resArr
