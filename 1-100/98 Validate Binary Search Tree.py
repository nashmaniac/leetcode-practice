from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def validate(self, root, max, min):
        if root is None:
            return True
        elif (max is not None and root.val >= max) or (min is not None and root.val <= min):
            return False
        else:
            return self.validate(root.left, root.val, min) and self.validate(root.right, max, root.val)


    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)




test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
