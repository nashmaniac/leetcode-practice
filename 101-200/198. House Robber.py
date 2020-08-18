from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0 for x in range(0, n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]



test_cases = [
    # [1,2,3,1],
    # [2,7,9,3,1]
    [2,1,1,2]
]

for t in test_cases:
    s = Solution().rob(t)
    print(t, s)
