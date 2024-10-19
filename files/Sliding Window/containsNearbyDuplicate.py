class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # cannot involve sorting input array because we need the indices
        # sliding window makes it so that instead of O(n^2), we do it in O(n)
        window_set = set()
        for i in range(len(nums)):
            if nums[i] in window_set:
                    return True
            window_set.add(nums[i])
            
            if len(window_set)>k:
                window_set.remove(nums[i-k])
                
        return False
