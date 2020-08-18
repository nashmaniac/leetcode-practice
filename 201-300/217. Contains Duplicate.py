from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums) == len(set(nums)))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        seen_list = dict()
        for i in range(0, len(nums)):
            if str(nums[i]) not in seen_list:
                seen_list.update(
                    **{
                        str(nums[i]): 1
                    }
                )
            else:
                return True
        return False

test_cases = [
    # [1, 2, 3, 1],
    [3, 3],
    # [],
    # [1, 2, 3, 4, 5]
]

for t in test_cases:
    s = Solution().containsDuplicate2(t)
    print(t, s)