# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        to_visit = deque()
        to_visit.append([root])
        while to_visit:
            nodes = to_visit.popleft()
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            new_row = []
            for n in nodes:
                if n.left:
                    new_row.append(n.left)
                if n.right:
                    new_row.append(n.right)
            if new_row:
                to_visit.append(new_row)

    def __init__(self):
        self.root = None

    def add(self, new_node, node):
        if not self.root:
            self.root = new_node
            return

        if new_node.val < node.val:
            if node.left:
                self.add(new_node, node.left)
            else:
                node.left = new_node
        else:
            if node.right:
                self.add(new_node, node.right)
            else:
                node.right = new_node

    def order(self, node):
        if not node:
            return

        yield from self.order(node.left)
        yield node.val
        yield from self.order(node.right)


so = Solution()
so.add(TreeLinkNode(2), so.root)
so.add(TreeLinkNode(1), so.root)
so.add(TreeLinkNode(3), so.root)
for i in so.order(so.root):
    print(i)
so.connect(so.root)
so.connect(so.root)
