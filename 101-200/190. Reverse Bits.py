from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        b = str(bin(0b11111111111111111111111111111101)[2:])[::-1]
        b = b.ljust(32, '0')
        return int(b, 2)


test_cases = [
    1
]

for t in test_cases:
    s = Solution().reverseBits(t)
    print(t, s)
