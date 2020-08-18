from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, int(len(s)/2)):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

test_cases = [
    ["h","e","l","l","o"]
]

for t in test_cases:
    s = Solution().reverseString(t)
    print(t, s)
