from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    best = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max([self.maxDepth(root.left), self.maxDepth(root.right)]) + 1


test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
