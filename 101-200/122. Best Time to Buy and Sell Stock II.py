from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += (prices[i+1]-prices[i])
        return profit


    def maxProfit_attempt2(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0

        if len(prices) == 1:
            return prices[0]

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit

test_cases = [
    [7, 1, 5, 3, 4, 6],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1],
]


for t in test_cases:
    s = Solution().maxProfit_attempt2(t)
    print(t, s)
