from typing import List

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)
        print(a, b)
        return a == b


test_cases = [
    ["anagram", "nagaram"],
    ["rat", "car"]
]

for t in test_cases:
    s = Solution().isAnagram(t[0], t[1])
    print(t, s)
