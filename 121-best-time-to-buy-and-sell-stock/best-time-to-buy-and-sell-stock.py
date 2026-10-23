class Solution(object):
    def maxProfit(self, prices):
        # 7 1 5 3 6 4
        #  
        minimax = float('inf')
        profit = 0

        for price in prices:
            if price < minimax:
                minimax = price #1

            current_profit = price - minimax # 6-1=5

            if current_profit > profit:
                profit = current_profit #4

        return profit

        # for i in range(n):
        #     if prices[i]>prices[i+1]:
        #         mini = prices[i+1] #4

        #     else: # prices[i]<prices[i+1]
        #         mini = prices[i] #3
            
        #     mini_max = min(mini,mini_max) #1
        #     profit = max(profit,prices[i+1]- mini_max) # max(5)
        
        # return profit

            




        """
        :type prices: List[int]
        :rtype: int
        """
        