class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def pre_order_traversal(self, node):
        print(node.value, end=' ')
        if node.left:
            self.pre_order_traversal(node.left)
        if node.right:
            self.pre_order_traversal(node.right)
        return

    def in_order_traversal(self, node):
        if node.left:
            self.in_order_traversal(node.left)
        print(node.value, end=' ')
        if node.right:
            self.in_order_traversal(node.right)
        return

    def post_order_traversal(self, node):
        if node.right:
            self.post_order_traversal(node.right)

        print(node.value, end=' ')

        if node.left:
            self.post_order_traversal(node.left)

        return

    def check_valid_node(self, node):
        # leaf node
        if node.left is None and node.right is None:
            return True

    def is_valid_bst(self):
        return self.check_valid_node(self.root)

    def depth(self, count, node):
        if node is None:
            return count
        return max(self.depth(count + 1, node.left), self.depth(count + 1, node.right))

    def find_depth(self):
        node = self.root
        count = 0
        return max(self.depth(count + 1, node.left), self.depth(count + 1, node.right))




'''
                     2
                    / \
                    3  3
                   / \ / \
                   1 3 1  3
'''

tree = Tree(5)
tree.root.left = Node(2)
tree.root.right = Node(8)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(6)
tree.root.right.right = Node(9)

# 5 2 1 3 8 6 9
tree.pre_order_traversal(tree.root)
print()
tree.in_order_traversal(tree.root)
print()

tree.post_order_traversal(tree.root)

print(tree.find_depth())
