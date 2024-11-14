class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynammic programming, literally the same as coin change
        # we can either choose to take if we havent taken anything left of us yet
        # otherwise, we just take the current sum and make it equal to current val
        # must start at index i = 2
        # take the maximum of current element  and element that is 2 behind it (the sum) and sum of -1 position
        # example [1,2 ,3 ,1]
        #  start at 3
        #  we 'take' the maximumum of 3+1 and 2 
        # make the value at index 2 equal to 3+1 = 4
        # so currentMax is 4
        # now at index 3 (we took something next to us btw)
        # we calculate 2+1 and see if it is greater than what we placed at index 2 (4)
        # example [2,7,9,3,1]
        # start at index 2
        # we take the max of (9+2) vs 7..
        # 11 is bigger, so we place 11 at index 2
        # now at index 3
        # check max between (3+7) and index before (11)
        # 11 is bigger, so we replace val at index 3 with 11
        # now at index 4
        # check 1 + 11 vs 11, we see 1 + 11 is greater, so we replace current element
        # now return the last element in the list

      # insert here in the case that a beginning house has more money than other houses after it 
        nums.insert(0,0)
       
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[len(nums)-1]




        
