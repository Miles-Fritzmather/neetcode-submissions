class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        
        buy = 0
        sell = 1
        best = 0
        while sell < len(prices):
            best = max(best, prices[sell] - prices[buy])
        
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                sell += 1
            
            
            
        return best