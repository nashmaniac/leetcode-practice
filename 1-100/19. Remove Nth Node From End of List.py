from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(0, n):
            first = first.next

        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next





test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
