# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, ne=None):
        self.val = x
        self.next = ne


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        cur = head
        prev = None
        while True:
            if cur and cur.next:
                n1 = cur
                n2 = cur.next
                n3 = cur.next.next

                n2.next = n1
                n1.next = n3
                if prev:
                    prev.next = n2
                prev = n1
                cur = n3
                if head == n1:
                    head = n2
            elif cur:
                if prev:
                    prev.next = cur
                return head
            else:
                break

        return head


def test_swapPairs():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [2, 1, 4, 3])


def test_swapPairs_2():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [2, 1, 4, 3, 5])


def test_swapPairs_3():
    head = None

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [])


def test_swapPairs_4():
    head = ListNode(1)

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [1])


def test_swapPairs_5():
    head = ListNode(1, ListNode(2))

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [2, 1])


def test_swapPairs_6():
    head = ListNode(1, ListNode(2, ListNode(3)))

    head = Solution().swapPairs(head)
    n = head
    res = []
    while n:
        res.append(n.val)
        n = n.next

    assert(res == [2, 1, 3])
