class Solution(object):
    def maxProfit2(self, prices):
    #This is buy and sell stock 2
      #Notes
      #   #Imagine you were a stock trader and you know the future prices for a given stock
        # (This is the problem input).
        # Each day you would buy the stock if you knew you could sell it tomorrow for a profit
        # (This is the greedy solution).
        """
        :type prices: List[int]
        :rtype: int
        """
        add = 0
        profit = 0
       

        for i in range(len(prices)-1):
            if prices[i+1]-prices[i] >0:
                profit +=prices[i+1]-prices[i]
           
                

        return profit
      

        
