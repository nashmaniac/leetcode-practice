from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_list = []
        for i in range(0, len(nums)):
            if not final_list:
                final_list.append(nums[i])
            else:
                final_list.append(max(nums[i], final_list[i-1]+nums[i]))

        return max(final_list)


test_cases = [
    [-2,1,-3,4,-1,2,1,-5,4]
]

for t in test_cases:
    s = Solution().maxSubArray(t)
    print(t, s)
