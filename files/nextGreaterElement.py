class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # how would I brute force this
        # nums2 has all the elements of nums1
        #need to find an index-->>sounds bin search?
        #index where nums1[i] == nums2[j]
        # find the next biggest element of nums2[j] in nums2

        #do we iterate through len(nums1) as directed

        #find values through 2 for loops
        #found the values, 
                    #now we need to find for the rest of nums2, if there's an element greater than our value nums2[j]
                    # once it finds the next biggest one, we change teh ith part of the array to this, and break 
        index = 0
        resArr = [-1]*len(nums1)
        nextGreater = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        if nums2[k]>nums2[j]:
                            resArr[i] = nums2[k]
                            break

        return resArr
