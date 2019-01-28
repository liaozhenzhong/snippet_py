class PrefixTree(object):
    def __init__(self):
        self.data = dict()


    def insert(self, word, node):
        if not word:
            node['done'] = None
            return
        c = word[0]
        if c not in node:
            node[c] = dict()
        self.insert(word[1:], node[c])


    def show(self, node, prefix):
        if not node:
            return
        if 'done' in node:
            yield prefix
        for k, v in node.items():
            yield from self.show(v, prefix + k)


    def show_complete(self, keyword):
        cur = self.data
        prefix = []
        for i in keyword:
            if i not in cur:
                return
            cur = cur[i]
            prefix.append(i)
        yield from self.show(cur, ''.join(prefix))
