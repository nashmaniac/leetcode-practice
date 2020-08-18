from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        move_count = 0
        while count < len(nums):
            if nums[move_count] != 0:
                move_count += 1
            else:
                nums.append(nums.pop(move_count))
            count+=1


nums = [0,0,1]
s = Solution().moveZeroes(nums)
print(nums)