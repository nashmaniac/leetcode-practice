from typing import List

import collections
class Solution:
    def hammingWeight(self, n: int) -> int:
        pass
        


test_cases = [
    '00000000000000000000000000001011',
    '00000000000000000000000010000000',
    '11111111111111111111111111111101'
]

for t in test_cases:
    s = Solution().hammingWeight(int(t))
    print(t, s)
