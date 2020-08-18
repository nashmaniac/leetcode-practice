from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value_map = {

        }
        for i in nums:
            try:
                value_map[str(i)] += 1
            except Exception as exc:
                value_map = dict(
                    value_map, **{
                        str(i): 1
                    }
                )
        v = [key for key in value_map if value_map[key] == 1]
        return v[0]

    def singleNumber3(self, nums: List[int]) -> int:
        value_map = dict()

        for i in range(0, len(nums)):
            if str(nums[i]) not in value_map:
                value_map.update(**{
                    str(nums[i]): 1
                })
            else:
                value_map.update(**{
                    str(nums[i]): value_map[str(nums[i])]+1
                })

        for i in value_map:
            if value_map[i] == 1:
                return int(i)



    def singleNumber2(self, nums: List[int]) -> int:
        return 2*sum(list(set(nums))) - sum(nums)

test_cases = [
    [2, 2, 1],
]

for t in test_cases:
    s = Solution().singleNumber3(t)
    print(s)