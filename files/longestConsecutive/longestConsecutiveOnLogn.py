
class Solution(object):
    def longestConsecutiveOnLogn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use get or default for hashmap?
        #first, how would we solve on >O(n)
            #sort the list, loop through, keep a count, if the next element is not 1 more then stop the count

        nums.sort()
        if(len(nums) == 1):
            return 1
        count = 1
        maximum = 0
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
              

            elif nums[i] == nums[i - 1]:
                if count>maximum:
                    maximum = count
                continue

            else:
                count = 1

            if count > maximum:
                maximum = count
                
        return maximum
            
