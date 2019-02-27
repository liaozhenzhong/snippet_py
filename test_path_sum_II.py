class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'List[List[int]]':
        self.travel(root, [], sum)
        return self.result

    def travel(self, node, path, remaining):
        if not node:
            return

        if not node.left and not node.right and node.val == remaining:
            self.result.append(path + [node.val])

        if node.left:
            self.travel(node.left, path + [node.val], remaining - node.val)
        if node.right:
            self.travel(node.right, path + [node.val], remaining - node.val)
        
def test_pathsum_1():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    so = Solution()
    print(so.pathSum(root, 22))

def test_pathsum_2():
    root = None
    so = Solution()
    print(so.pathSum(root, 1))

test_pathsum_2()
