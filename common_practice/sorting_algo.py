from typing import List

import random
import time, math


class Solution:

    def bubble_sort(self, nums):
        s = time.time()
        print(nums)
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
            print(i, '-', nums)
        return (time.time() - s) * math.pow(10, 3), nums

    def merge(self, nums, start, mid, end):
        n1 = mid - start + 1
        n2 = end - mid

        l = [nums[start + x] for x in range(0, n1)]
        r = [nums[mid + 1 + x] for x in range(0, n2)]

        print('Left: ', l, ' Right: ', r)
        i = j = 0
        k = start
        while i < n1 and j < n2:
            if l[i] < r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1

            k += 1
        while i < n1:
            nums[k] = l[i]
            i += 1
            k += 1

        while j < n2:
            nums[k] = r[j]
            k += 1
            j += 1

    def merge_sort(self, nums, start, end):
        if start < end:
            mid = start + (end - start) // 2
            # print(start, mid, end)

            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)
            print(nums)

    def partition(self, nums, start, end):
        pivot = nums[end]
        index = start - 1
        counter = start
        while counter < end:
            if nums[counter] <= pivot:
                index += 1
                nums[index], nums[counter] = nums[counter], nums[index]
            counter += 1
        nums[index + 1], nums[counter] = nums[counter], nums[index + 1]
        print(nums)
        return index + 1

    def quick_sort(self, nums, start, end):
        if start < end:
            p = self.partition(nums, start, end)
            self.quick_sort(nums, start, p - 1)
            self.quick_sort(nums, p + 1, end)
            # print(nums)

    def selection_sort(self, nums):
        for i in range(0, len(nums)):
            index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[index]:
                    index = j

            nums[index], nums[i] = nums[i], nums[index]
            print(nums)

    def sort(self, nums, method='bubble'):
        if method == 'selection':
            s = time.time()
            self.selection_sort(nums)
            print(nums)
            return (time.time() - s) * math.pow(10, 3), nums
        if method == 'merge':
            s = time.time()
            self.merge_sort(nums, 0, len(nums) - 1)
            print(nums)
            return (time.time() - s) * math.pow(10, 3), nums

        if method == 'quick':
            s = time.time()
            self.quick_sort(nums, 0, len(nums) - 1)
            print(nums)
            return (time.time() - s) * math.pow(10, 3), nums

        return self.bubble_sort(nums)


test_cases = [
    list(range(0, 10))
]

for t in test_cases:
    random.shuffle(t)
    s = Solution().sort(list(t), method='selection')
    print('---------------')
    print('Input: ', t)
    print('Output: ', s[1])
    print('Time: ', '%.2f ms' % s[0])
