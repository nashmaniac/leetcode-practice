from typing import List


class Solution:

    def reverse(self, nums: List[int], start:int, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
        return nums



    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            nums.insert(0, nums.pop())
        n = len(nums)
        nums = self.reverse(nums, 0, n-1)
        nums = self.reverse(nums, 0, k-1)
        nums = self.reverse(nums, k, n-1)
        # print(nums)




test_cases = [
    ([1,2,3,4,5,6,7], 3),
    ([-1,-100,3,99], 2)
]

for t in test_cases:
    s = Solution().rotate(t[0], t[1])
    print(s)