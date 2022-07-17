class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain = 0
        a = prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p > a:
                gain += p - a
            a = p
        return gain
