class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        check = 0
        #skip values that are value
        #pointer continues to incrmeent
        #stop at pointer that aren't val
        #continue iterate through array, once you get to value thats val 
        #THE COUNT SERVES AS THE PLACE WHERE WE LAST SAW SOMETHING EQUAL TO TARGET
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
               
        return count
