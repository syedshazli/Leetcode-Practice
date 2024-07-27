
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right = max(piles)
        result = right
        # for a fixed speed k bannas per hour
        #math.ceil(4.2) this rounds up for us, which is what we want
      

        #while this is true, we see if the middle speed per hour gets us there in time.
        # If the current k takes too long, adjust right bound to k-1
        # If the current k takes too short, adjust left bound to k+1
        while left <=right:
            hours = 0
            midBan = (left+right)//2

            for i in range(len(piles)):
                hours += math.ceil(piles[i]/midBan)
    
            if hours <= h:
                result = min(result, midBan)
                right = midBan-1 #took too long to eat, midBan is too low, increase left bound
          
            else:
               #took too short to eat
               left = midBan+1

        return result
