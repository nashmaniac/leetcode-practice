from typing import List


class Solution:
    def isBadVersion(self, n):
        version = 1702766719
        return not (n < version)

    def firstBadVersion(self, n):
        num_list = list(range(1, n+1))
        print(num_list)
        while len(num_list) != 1:
            lowest = 0
            highest = len(num_list)-1
            mid = int((highest+lowest) / 2)

            if self.isBadVersion(num_list[mid]):
                num_list = num_list[:mid+1]
            else:
                num_list = num_list[mid+1:]
        return num_list[0]




test_cases = [5]

for t in test_cases:
    s = Solution().firstBadVersion(2126753390)
    print(t, s)
