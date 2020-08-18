from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        firstOne = strs[0]
        final_value = ''
        test_value = ''
        for i in firstOne:
            found = True
            test_value+=i
            for j in strs[1:]:
                if not j.startswith(test_value):
                    found = False
                    break
            if not found:
                break

            if len(test_value) > len(final_value):
                final_value = test_value

        return final_value


s = Solution().longestCommonPrefix(["flower","flow","flight"])
print(s)