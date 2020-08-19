from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        value_map = dict()
        for i in range(0, len(numbers)):
            comp = target - numbers[i]
            if str(comp) not in value_map:
                value_map.update(**{
                    str(numbers[i]): i+1
                })
            else:
                return [value_map[str(comp)], i+1]




test_cases = [
    ([2,7,11,15], 9)
]

for t in test_cases:
    s = Solution().twoSum(t[0], t[1])
    print(t, s)
