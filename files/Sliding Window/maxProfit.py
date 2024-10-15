class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # In here I did a greedy approach where if it was a higher price the next day, sell
        # but what is a sliding window approach?
        # sliding window allows you to not recompute values 
        # sell =True if we decide to sell 
        # create buy index
        # what window size
        # 
        # for i in range(len(prices)-2):
        #   for j in range(i, len(prices)-1):
        #           Price = prices[j]-prices[j]
        #           maxPrice = max(maxPrice, Price)
        # return maxPrice
    

        maxPrice = 0
        Price = 0
       #So we see if the price is the lowest we've seen, 
       #and if so, try to see if the currentPrice-lowestPrice is greater than the maximumPrice
       #and if so set Maximum Price to this?
        lowest = prices[0]
        maxPrice = 0
        current = 0
        for i in range(1,len(prices)):
            lowest = min(lowest,prices[i])
            current = prices[i]-lowest
            maxPrice = max(current, maxPrice)
        return maxPrice
        # for i in range(1,len(prices)):
        #   lowest = min(lowest, prices[i])
        #   current = prices[i]-lowest
        #   maxPrice = max(current,maxPrice)
        #return maxPrice
