class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the index of the smallest element
        pivot = self.findMin(nums)
        
        # Perform binary search in the appropriate half
        if nums[pivot] <= target <= nums[-1]:
            # Search in the right half
            return self.binarySearch(nums, target, pivot, len(nums) - 1)
        else:
            # Search in the left half
            return self.binarySearch(nums, target, 0, pivot - 1)

    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            middle = (low + high) // 2
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle
        
        return low

    def binarySearch(self, nums: List[int], target: int, low: int, high: int) -> int:
        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        
        return -1
