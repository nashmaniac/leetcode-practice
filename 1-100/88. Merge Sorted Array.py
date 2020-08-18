from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n> 0:
            i = m - 1
            j = n - 1
            k = (m + n) - 1

            while i > -1 and j > -1:

                if nums1[i] < nums2[j]:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
                k -= 1
            while i > -1:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            while j > -1:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1


        if m == 0:
            for i in range(0, n):
                nums1[i] = nums2[i]


test_cases = [
    # [[1,2,3,0,0, 0], 3, [2,5,6], 3],
    # [[0], 0, [1], 1],
    [[2, 0],1, [1],1]
]

for t in test_cases:
    s = Solution().merge(t[0], t[1], t[2], t[3])
    print(t, t[0])
