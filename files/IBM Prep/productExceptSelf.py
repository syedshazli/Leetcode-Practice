class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we know not to include the current element
        # the reason why division helps is bc you can just:
        #    calculate the total product for each element and store in array
        #       for each element, append the total product divided by current element

        #but this isnt possible due to constraints of problem
        # can calculate product of whats on the left of each element 
        # and multiply by product of whats on the right of each element

        # my issue is how do we do so that it's uniquely for each value in the array?
        prefixArr = [1] *len(nums)
        postfixArr = [1]*len(nums)
        resultArr = [1]*len(nums)

        #prefix loop, this works!
        currentNum = 0
        for i in range(len(nums)):
            if i == 0:
                prefixArr[i] = 1
                currentNum = 1
            else:
                currentNum *= nums[i-1]
                prefixArr[i] = currentNum
        #print(prefixArr)

        #this works for postfix!
        postfixNum = 0
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums)-1:
                postfixArr[j] = 1
                postfixNum = 1
            else:
                postfixNum*= nums[j+1]
                postfixArr[j]=postfixNum
        
        
        for z in range(len(nums)):
            resultArr[z] = prefixArr[z]*postfixArr[z]


        #postfixLoop
        return resultArr
