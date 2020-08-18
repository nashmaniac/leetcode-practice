from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_height(self, node):
        if not node:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

    def depth(self, count, node):
        if node is None:
            return count
        return max(self.depth(count + 1, node.left), self.depth(count + 1, node.right))

    def get_height_2(self, node):
        count = 0
        return max(self.depth(count + 1, node.left), self.depth(count + 1, node.right))

    def level_order(self, level, node):
        if node is None:
            return []
        if level == 0:
            # print(node.val)
            return [node.val]
        if level >= 1:
            c = []
            d = []
            if node.left:
                c = self.level_order(level - 1, node.left)
            if node.right:
                d = self.level_order(level - 1, node.right)
        return c+d


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        height = self.get_height(root)
        final_list = []
        for i in range(0, height):
            c=self.level_order(i, root)
            final_list.append(c)
        return final_list


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(10)

print(Solution().levelOrder(root))
