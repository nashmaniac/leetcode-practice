from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        num_list = [
            x for x in range(2, n)
        ]

        for index, i in enumerate(num_list):
            if i is None:
                continue
            j = index + i
            while (j+2) < n:
                try:
                    num_list[j] = None
                    j += i
                except Exception as exc:
                    print(i, j)

        num_list = len(list(filter(lambda x: x is not None, num_list)))
        return num_list

test_cases = [
    10
]

for t in test_cases:
    s = Solution().countPrimes(t)
    print(t, s)
