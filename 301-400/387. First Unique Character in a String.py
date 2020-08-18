from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        value_map = dict()
        s = s.lower()
        for index, c in enumerate(s):
            if c in value_map:
                value_map[c]+=1
            else:
                value_map = dict(
                    value_map, **{
                        str(c): 1
                    }
                )

        for index, c in enumerate(s):
            if value_map[c] == 1:
                return index

        return -1

test_cases = [
    "aadadaad",
    "leetcode", "loveleetcode", "",
]

for t in test_cases:
    s = Solution().firstUniqChar(t)
    print(t, s)
