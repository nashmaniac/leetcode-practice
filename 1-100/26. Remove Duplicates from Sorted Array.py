from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start_index = 0
        for index, i in enumerate(nums[1:]):
            if nums[index] < nums[index+1]:
                start_index += 1
                nums[start_index] = nums[index+1]
        return start_index+1


    def removeDuplicates_attempt2(self, nums: List[int]) -> int:
        end = 0
        for i in range(0, len(nums)-1):
            if nums[i+1] > nums[i]:
                end += 1
                nums[end] = nums[i+1]
        return end+1


test_cases = [
    [0,0,1,1,1,2,2,3,3,4], [1, 1, 2]
]

for t in test_cases:
    s = Solution().removeDuplicates_attempt2(t)
    print(t, s)