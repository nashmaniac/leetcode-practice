from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_rep = str(bin(x)[2:])
        y_rep = str(bin(y)[2:])

        max_len = max(len(x_rep), len(y_rep))

        x_rep = x_rep.zfill(max_len)
        y_rep = y_rep.zfill(max_len)

        distance = 0
        for i in range(len(x_rep)):
            if x_rep[i] != y_rep[i]:
                distance += 1
        return distance


test_cases = [
    [4, 6], [1, 4]
]

for t in test_cases:
    s = Solution().hammingDistance(t[0], t[1])
    print(t, s)
