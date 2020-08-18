from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        start_index = -1
        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                start_index = i
                break
        return start_index


test_cases = [
    ["hello", "ll"],
    ["aaaaa", "bba"],
    ["aaa", "aaaaa"],
]

for t in test_cases:
    s = Solution().strStr(t[0], t[1])
    print(t, s)
