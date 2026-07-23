class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0

        for i in range(len(prices)):
            buy: int = prices[i]
            for j in range(i + 1, len(prices)):
                sell: int = prices[j]
                max_profit = max(max_profit, sell - buy)
        
        return max_profit