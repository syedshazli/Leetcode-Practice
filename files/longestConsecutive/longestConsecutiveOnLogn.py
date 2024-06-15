
class Solution(object):
    def longestConsecutiveOnLogn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use get or default for hashmap?
        #first, how would we solve on >O(n)
            #sort the list, loop through, keep a count, if the next element is not 1 more then stop the count

       if len(nums) == 0:
            return 0

        nums.sort()

        if len(nums) == 1:
            return 1

        count = 1
        max_count = 1  # Initialize max_count to 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1

            if count > max_count:
                max_count = count

        return max_count
       
            
