from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = left + n

        final_list = []
        for i in range(0, n):
            final_list.append(nums[left])
            final_list.append(nums[right])
            left += 1
            right += 1
        return final_list


test_cases = [
    [[2,5,1,3,4,7], 3]
]

for t in test_cases:
    s = Solution().shuffle(t[0], t[1])
    print(t, s)
