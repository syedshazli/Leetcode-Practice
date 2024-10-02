class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I think this is more of a 3 pointer problem.
        # however, the third pointer will just be (left+right)//2
        # make a resultArray that's a 2D array []
        # say while left < right again
        # just a search problem with a target of 0
        # middle = (left+right)//2
        # if nums[left]+nums[right]+nums[middle] >0:
        # number is too high, set right pointer -=1
        # elif nums[left]+nums[right]+nums[middle]<0:
        # number is too low, set left +=1
        # else: resArr.append(nums[left], nums[right],nums[middle])
        # do note that input array is also not sorteddddd
        #return resArr
        nums.sort()
        print(nums)
        resArr = []
        left  = 0
        right = len(nums)-1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                currentSum = nums[left]+nums[right]+nums[i]
                if currentSum> 0:
                    right -=1
                elif currentSum <0:
                    left +=1
                else:
                    resArr.append([nums[left], nums[right], nums[i]])
                    left +=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                    right -=1
                # if current == right or current == left:
                #     continue 
                #what do we do once we find a valid solution
                #Initialize two pointers j and k to point to the elements next to the current element i and at the end of the array, respectively
                
            
                
                
        return resArr
