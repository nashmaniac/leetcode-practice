from typing import List


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next




test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
