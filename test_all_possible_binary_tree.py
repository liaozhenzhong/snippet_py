from pprint import pprint
from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def __init__(self):
        self.timer = 0

    def travel(self, node):
        if node:
            yield node
            yield from self.travel(node.left)
            yield from self.travel(node.right)

    def tick(self):
        self.timer += 1
        return self.timer


    def _allPossibleFBT(self, N):
        if N == 1:
            yield TreeNode(self.tick())

        if N%2 == 0:
            return None

        for i in range(1, N-1, 2):
            j = N - 1 - i
            for l in self._allPossibleFBT(i):
                for r in self._allPossibleFBT(j):
                    t = TreeNode(self.tick())
                    t.left = l
                    t.right = r
                    yield t


    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        for node in self._allPossibleFBT(N):
            for sub in self.travel(node):
                print(sub, sub.left, sub.right)
            print()

Solution().allPossibleFBT(7)