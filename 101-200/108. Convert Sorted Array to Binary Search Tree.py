from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def construct_tree(self, root, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        lower = nums[:mid]
        higher = nums[mid + 1:]
        node = TreeNode(nums[mid])
        node.left = self.construct_tree(node, lower)
        node.right = self.construct_tree(node, higher)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums)//2
        lower = nums[:mid]
        higher = nums[mid+1:]
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(lower)
        node.right = self.sortedArrayToBST(higher)
        return node

    def get_depth(self, root):
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right))+1

    def level_order(self, level, node):
        if not node:
            return
        if level == 0:
            print(node.val)
            return [node.val]
        if level >= 1:
            c = d = []
            if node.left:
                c = self.level_order(level - 1, node.left)
            if node.right:
                d = self.level_order(level - 1, node.right)
            return c+d

    def printLevelOrder(self, node):
        height = self.get_depth(node)
        final_list = []
        for i in range(0, height):
            c = self.level_order(i, node)
            final_list.append(c)
        return final_list




test_cases = [
    [1, 2, 3, 4, 5, 6]
]

for t in test_cases:
    s = Solution().sortedArrayToBST(t)
    print(Solution().get_depth(s))
    print(Solution().printLevelOrder(s))
    print(t, s)
