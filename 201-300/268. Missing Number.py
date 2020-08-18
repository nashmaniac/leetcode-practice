from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_count = len(nums)
        sum_count = int((num_count*(num_count+1))/2)
        return sum_count-sum(nums)

test_cases = [[
    0, 1, 3, 4,
], [0], [3,0,1], [9,6,4,2,3,5,7,0,1]]

for t in test_cases:
    s = Solution().missingNumber(t)
    print(t, s)
