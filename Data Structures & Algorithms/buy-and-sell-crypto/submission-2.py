class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0

        for i in range(len(prices)):
            buy: int = prices[i]
            for j in range(i + 1, len(prices)):
                sell: int = prices[j]
                profit = max(profit, sell - buy)
        
        return profit