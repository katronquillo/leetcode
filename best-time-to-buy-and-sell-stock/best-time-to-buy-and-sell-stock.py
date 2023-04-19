class Solution:
    """
    Input: Array of int stock prices
    Output: Maximum profit 

    Algorithm...
    1. Keep track of days to buy and sell
        - Initialized as B = 0 and S = 1
    2. Keep track of the maximumProfit seen so far
    3. If profit < 0, then we found a better day to buy stock
        - Change B = S and S = S + 1
    4. If profit >= 0, shift S
    5. Continue until S reaches the end of the list 
    """
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        while (sell < len(prices)):
            currProfit = prices[sell] - prices[buy]

            if (currProfit > maxProfit):
                maxProfit = currProfit

            if (currProfit < 0):
                buy = sell

            sell += 1
        return maxProfit
        