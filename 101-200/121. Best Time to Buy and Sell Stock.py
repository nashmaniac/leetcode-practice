from typing import List

import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        min_sum = float('inf')
        for i in range(0, len(prices)):
            if prices[i] < min_sum:
                min_sum = prices[i]
            else:
                max_sum = max(max_sum, prices[i]-min_sum)
        return max_sum

test_cases = [
    [7,1,5,3,6,4],
    [1, 2, 3, 4, 5],
    [7, 6, 4, 3, 1],
]


for t in test_cases:
    s = Solution().maxProfit(t)
    print(t, s)
