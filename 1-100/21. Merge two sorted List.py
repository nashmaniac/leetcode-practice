from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while l1 is not None and l2 is not None:
            if (l1.val < l2.val):
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        if l1 is not None:
            dummy.next = l1
        else:
            dummy.next = l2
        return head.next


test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
