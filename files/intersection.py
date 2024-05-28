class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #probably could do this in one line via python methods and intersection
        #but thats too easy and cheating!

        #make a new list and append everything from nums1 onto it

        #make a new loop looping through nums2, if element is not present in array then remove it

        newlist = []
        
        for number in range(len(nums2)):
            if nums2[number] in nums1 and nums2[number] not in newlist:
                newlist.append(nums2[number])

        return newlist
     
