from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_list = []

        for i in range(0, numRows):
            t = []
            if i >= 1:
                t.append(1)
                base_array = final_list[i-1]
                for i in range(0, len(base_array)-1):
                    t.append(base_array[i]+base_array[i+1])
            t.append(1)
            final_list.append(t)
        return final_list




test_cases = [5]

for t in test_cases:
    s = Solution().generate(t)
    print(t, s)
