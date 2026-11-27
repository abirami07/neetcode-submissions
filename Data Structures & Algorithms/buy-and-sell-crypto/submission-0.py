class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        left = prices[i] #left is the day we buy
        
        max_profit = 0

        while i+1 < len(prices):
            right = prices[i+1] #right is the day we sell
            if left < right:
                profit = right - left
                max_profit = max(max_profit, profit)
            else:
                left = right 
    
            i += 1
    
        return max_profit

            