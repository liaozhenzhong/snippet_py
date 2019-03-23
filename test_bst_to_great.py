# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def travel(self, node, acc):
        if node.right:
            acc = self.travel(node.right, acc)
        acc += node.val
        node.val = acc
        if node.left:
            acc = self.travel(node.left, acc)
        return acc

    def convertBST(self, root):
        if not root:
            return
        self.travel(root, 0)

    def display(self, node):
        if node.left:
            yield from self.display(node.left)
        yield node
        if node.right:
            yield from self.display(node.right)

def test_convertBST_1():
    root = TreeNode(5, TreeNode(2), TreeNode(13))
    Solution().convertBST(root)
    assert [20, 18, 13] == [i.val for i in Solution().display(root)]

def test_convertBST_2():
    root = None
    Solution().convertBST(root)

def test_convertBST_3():
    root = TreeNode(2, TreeNode(0, TreeNode(-4), TreeNode(1)), TreeNode(3))
    Solution().convertBST(root)
    assert [2, 6, 6, 5, 3] == [i.val for i in Solution().display(root)]

