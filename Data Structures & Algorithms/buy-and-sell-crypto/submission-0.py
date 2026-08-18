class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        minimum_prev = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - minimum_prev)
            minimum_prev = min(minimum_prev, prices[i])
        return max_profit