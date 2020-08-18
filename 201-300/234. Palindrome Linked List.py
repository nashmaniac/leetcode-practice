from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, node):
        prev_node = None
        curr_node = node
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node

    def isPalindrome(self, head: ListNode) -> bool:
        first = head
        second = head

        while first is not None and first.next is not None:
            first = first.next.next
            second = second.next

        rev_head = self.reverse_list(second)

        while rev_head is not None and head is not None:
            if rev_head.val != head.val:
                return False
            rev_head = rev_head.next
            head = head.next
        return True


test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
