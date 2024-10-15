class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # k ==2 we dont have to check, we just have to make sure we only calculate every 2
        # but how do we get sum from nums[i:i+k]
        nums = str(num)
        kbeaut = 0
        i = 0
        while i <len(nums):
          frame = "".join(nums[i:i+k])
         # print(frame)
        #   if nums[i] == 0:
        #     i+=1
        #     continue
          if int(frame) != 0 and len(frame) == k and num%int(frame) == 0:
            print(frame)
            kbeaut+=1
          i+=1
        
         #   i+=1
        return kbeaut
        
