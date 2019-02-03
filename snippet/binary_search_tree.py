class NodeBST(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self.root = None

    def add(self, new_node, node):
        if not self.root:
            self.root = new_node
            return

        if new_node.key < node.key:
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
        yield node.key
        yield from self.order(node.right)


t = BST()
for i in [3, 1, 5, 0, 2, 4, 6]:
    t.add(NodeBST(i), t.root)
for i in t.order(t.root):
    print(i, end=', ')
