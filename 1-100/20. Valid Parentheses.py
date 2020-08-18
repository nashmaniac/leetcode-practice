class Solution:
    def isValid(self, s: str) -> bool:
        ending_list = [')', '}', ']']
        maps = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        keep_list = []
        for i in s:
            if i in ending_list:
                try:
                    b = keep_list.pop()
                    if maps[i] != b:
                        return False
                except Exception as exc:
                    return False
            else:
                keep_list.append(i)

        return True if not keep_list else False


test_cases = [
    # "){", "({)", ")[",
    # "[]{()}"
    "{{)}"
]

for t in test_cases:
    s = Solution().isValid(t)
    print(t, s)
