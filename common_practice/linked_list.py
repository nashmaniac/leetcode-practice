class LinkNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def print_list(self, node):
        while node is not None:
            print(node.val, end='->')
            node = node.next
        print(None)

    def reverse_list(self, node):
        prev_node = None
        curr_node = node
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node

    def reverse_list_recursive(self, node):
        if node is None or node.next is None:
            return node

        rev_head = self.reverse_list_recursive(node.next)
        node.next.next = node
        node.next = None
        return rev_head

    def find_node(self, head, value):
        curr = head
        while curr is not None:
            if value == curr.val:
                return curr
            curr = curr.next
        return None

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def remove_nth_node(self, head, n):
        dummy = LinkNode(-1)
        dummy.next = head
        first = head
        second = head

        for i in range(0, n):
            first = first.next

        while first.next is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

    def find_palindrome(self, head):
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

    def hasCycle(self, head: LinkNode) -> bool:
        seen_node = []
        curr = head
        while curr is not None:
            if curr in seen_node:
                return True
            seen_node.append(curr)
            curr = curr.next
        return False

l1 = LinkNode(val=0)

parent = l1
for i in range(1, 10):
    m = LinkNode(i)
    parent.next = m
    parent = m

six_node = Solution().find_node(l1, 6)
Solution().delete_node(six_node)
Solution().print_list(l1)

rev_head = Solution().reverse_list_recursive(l1)
Solution().print_list(rev_head)
updated_head = Solution().remove_nth_node(rev_head, 3)
Solution().print_list(updated_head)

m1 = LinkNode(val=1)
parent = m1
for i in list("221"):
    m = LinkNode(int(i))
    parent.next = m
    parent = m

m.next = m1

print(Solution().hasCycle(m1))
