from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        r = None
        while n > 0:
            n = n // 3
            r = n % 3
        return True if r == 0 else False


test_cases = [
    81, 0, 1, 5,
    27,
    45
]

for t in test_cases:
    s = Solution().isPowerOfThree(t)
    print(t, s)
