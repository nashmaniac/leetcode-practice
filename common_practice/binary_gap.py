from typing import List


class Solution:
    def solution(self, N):
        # write your code in Python 3.6
        length_list = []
        first_occurance = False
        s = str(bin(N)[2:])
        count = 0
        for i in s:
            if int(i) == 1:
                if not first_occurance:
                    first_occurance = True
                else:
                    # pop now
                    if count > 0:
                        length_list.append(count)
                        first_occurance = False
            else:
                count += 1
        return max(length_list) if length_list else 0

    def recurse(self, num):
        if num <= 1:
            return 1

        return num*self.recurse(num-1)

    def numTilePossibilities(self, tiles: str) -> int:
        length = len(tiles)
        return self.recurse(length)


test_cases = [
    "AAB"
]

for t in test_cases:
    s = Solution().numTilePossibilities(t)
    print(t, s)
