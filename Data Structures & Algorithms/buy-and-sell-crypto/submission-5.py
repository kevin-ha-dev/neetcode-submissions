class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left: int = 0
        right: int = 1
        max_profit: int = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right+=1
        return max_profit