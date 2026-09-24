class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_pf = 0
        for i in range(0, l):
            for j in range(i+1, l):
                if prices[i] <= prices[j]:
                    profit = prices[j] - prices[i]
                    if profit > max_pf:
                        max_pf = profit
        return max_pf
