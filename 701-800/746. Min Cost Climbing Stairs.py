from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]

        dp = [None for x in range(0, len(cost))]

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])

        return dp[len(cost)-1]




test_cases = [
    # [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]

for t in test_cases:
    s = Solution().minCostClimbingStairs(t)
    print(t, s)
