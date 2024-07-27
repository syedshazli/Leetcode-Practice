#Notes
# Python 3 solution
# This was a good problem for me. I initially had some trouble starting off but then I got really close with the algorithm.
# I used to have an if elif, else, similar to bin search. But it turns out you only need an if and else for updating the bounds
# then you can return the result outside the while loop. No need for returning inside although I'm sure it;s possible
# Make sure you round up. The left would be the minimum eating speed (1) and right would be highest number in the list.
# set the return variable to right in case we dont find success in our algorithm
# while the left var is less than or equal to right var, reset hours, and loop through the list, rounding up and adding  piles[i]/middle to hours
# This ensures we know how many hours it takes KOKO (after calcualting our middle) for the current speed "middle"
# adjust left and right based on what we get for hours. If it takes too short, decrease the right variable, else, increase the left variable 

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
