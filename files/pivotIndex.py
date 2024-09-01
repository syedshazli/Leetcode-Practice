#brute force:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0
        for i in range(len(nums)):
            leftSum = sum(nums[:i+1])
            print(leftSum)
            rightSum = sum(nums[i:])
            print(rightSum)
            if leftSum == rightSum:
                return i

        return -1
