class Solution(object):
    def twoSum(self, nums, target):
        correct = [0,0]
        newMap = dict()
        for i in range(len(nums)):
            sumVal = target - nums[i]
            if sumVal in newMap:
                correct[0] = i
                correct[1] = newMap[sumVal]
                break
            newMap[nums[i]] = i

        return correct

    #
    #
    #
