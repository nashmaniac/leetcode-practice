from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, i in enumerate(nums):
            found = False
            for j_index, j in enumerate(nums[index+1:]):
                if i+j == target:
                    found = True
                    break
            if found:
                break
        return [index, j_index+index+1]
    def two_sum_another(self, nums: List[int], target: int) -> List[int]:
        value_map = dict()

        for index, i in enumerate(nums):
            comp = target - i

            if str(i) in value_map:
                return [value_map[str(i)], index]
            else:
                value_map = dict(
                    value_map, **{
                        str(comp): index
                    }
                )



nums = [2, 7, 11, 15]
target = 9
s = Solution().two_sum_another(nums, target)
print(s)