from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseLinkedList(self, head) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            nextItem = curr.next
            curr.next = prev
            prev = curr
            curr = nextItem
        return prev

    def getIntValue(self, node: ListNode) -> int:
        curr = node
        result = ''
        while curr is not None:
            result += str(curr.val)
            curr = curr.next

        return int(result)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rev_l1 = self.reverseLinkedList(l1)
        rev_l2 = self.reverseLinkedList(l2)

        l1_value = self.getIntValue(rev_l1)
        l2_value = self.getIntValue(rev_l2)

        result = str(l1_value + l2_value)

        node = ListNode(int(result[0]))
        head = node
        for i in result[1:]:
            n = ListNode(int(i))
            node.next = n
            node = n
        return self.reverseLinkedList(head)


test_cases = []

for t in test_cases:
    s = Solution()
    print(t, s)
