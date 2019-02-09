# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        root = ListNode(None)
        root.next = head
        p = root
        while p:
            if not p.next or not p.next.next:
                break
            y = p.next
            while y and y.next and y.val == y.next.val:
                y = y.next
            if p.next == y:
                p = p.next
            else:
                if root.next == y.next:
                    root.next = y.next
                p.next = y.next

        return self.elements(root.next)

    def elements(self, head):
        elem = []
        p = head
        while p:
            elem.append(p.val)
            p = p.next
        return elem


def test_remove_dup():
    head = ListNode(5)
    for i in reversed([1, 2, 3, 3, 4, 4]):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node
    assert(Solution().deleteDuplicates(head) == [1, 2, 5])


def test_remove_dup_at_front():
    head = ListNode(3)
    for i in reversed([1, 1, 1, 1, 1, 2]):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node
    assert(Solution().deleteDuplicates(head) == [2, 3])


def test_remove_dup_at_end():
    head = ListNode(3)
    for i in reversed([1, 2, 3, 3, 2]):
        new_node = ListNode(i)
        new_node.next = head
        head = new_node
    assert(Solution().deleteDuplicates(head) == [1, 2, 2, 3])
