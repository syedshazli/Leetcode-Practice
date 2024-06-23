class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #recommended to do two sum II
        #BINARY SERCH 2 POINTERS GRRRR
        nums.sort()
        result = []
        n = len(nums)-1
        for i in range(n):
            target = -nums[i]
           
            j = i+1
            k = n
            if i>0 and nums[i] == nums[i-1]:
                continue
    
            while j<k:

                if target== nums[j] + nums[k]:

                    result.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                  
                elif nums[j] + nums[k] >target:
                    k-=1
                else:
                    #added to numbers to negative and it was too small. 
                    j+=1
                
        return result
