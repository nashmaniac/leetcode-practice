from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        prev_node = None
        next_node = None
        curr_node = head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node


    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        rev_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return rev_head




test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
