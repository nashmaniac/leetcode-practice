from typing import List
import collections


class Solution:
    value_map = dict()

    def countAndSay(self, n: int) -> str:
        if n == 1 or n == 0:
            self.value_map.update(**{
                '1': '1'
            })
            return '1'

        if str(n-1) in self.value_map:
            a = self.value_map.get(str(n-1))
        else:
            a = self.countAndSay(n - 1)

        count = 1
        s = ''
        for i in range(0,len(a)):
            if i == len(a) -1 or a[i] != a[i+1]:
                s += (str(count)+a[i])
                count = 1
            else:
                count += 1

        self.value_map.update(**{
            str(n): s
        })

        return s


test_cases = [1, 2, 3, 4, 5, 6, 7]

for t in test_cases:
    s = Solution().countAndSay(t)
    print(t, s)
