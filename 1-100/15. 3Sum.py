from typing import List

'''
Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        value_map = dict()
        final_list = []
        for i in range(0, len(nums)):
            pivot_num = nums[i]
            for j in range(0, len(nums)):
                if i != j:
                    current_num = nums[j]
                    key = [pivot_num, current_num]
                    if str(current_num) not in value_map:
                        value_map.update(**{
                           str(0-sum(key)): key
                        })
                    else:
                        temp_list = list(sorted(value_map[str(current_num)]+[current_num]))
                        if temp_list not in final_list:
                            final_list.append(temp_list)

        return final_list



test_cases = [
    [-1, 0, 1, 2, -1, -4]
]



for t in test_cases:
    s = Solution().threeSum(t)
    print(t, s)
