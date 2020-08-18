from typing import List

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = collections.Counter(nums1)
        b = collections.Counter(nums2)
        return list((a&b).elements())


test_cases = [
    [[1,2,2,1], [2,2]]
]

for t in test_cases:
    s = Solution().intersect(t[0], t[1])
    print(s)