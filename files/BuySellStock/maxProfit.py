class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = prices[0]
        maximum = 0
        for i in range(len(prices) -1):
            if(prices[i]<smallest):
                smallest = prices[i]
            
            if(prices[i+1]-smallest>maximum):
                maximum = prices[i+1]-smallest
        return maximum
