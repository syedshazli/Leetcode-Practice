class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # we want a hashmap to know what index we're at
        hashmap = dict()
        # could use the hashmap to store the next greatest element in nums2
        resArr = []
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if len(stack) == 0:
                hashmap[nums2[i]] = -1
            
            else:
                hashmap[nums2[i]] = stack[-1]

            stack.append(nums2[i])
        
        #iterate through nums1, appending value of hashmap[nums1[i]]
        for i in range(len(nums1)):
            resArr.append(hashmap[nums1[i]])

        return resArr
        
