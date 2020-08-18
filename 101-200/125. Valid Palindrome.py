from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        s = ''.join([x for x in s if x.isalnum()])
        if not s:
            return True

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


test_cases = [
    "A man, a plan, a canal: Panama",
    ".",
    " ",
    ""
]

for t in test_cases:
    s = Solution().isPalindrome(t)
    print(t, s)
