class DirNode(object):
    def __init__(self, name):
        self.is_folder = (name.find('.') == -1)
        self.name = name
        self.sub_nodes = []


class DirTree(object):
    def __init__(self):
        self.root = []
        self.last_path = []

    def add_item(self, name):
        path = name.split('\t')
        if len(path) == 1:
            new_node = DirNode(path[0])
            self.root.append(new_node)
            self.last_path = [new_node]
            return

        for i in range(len(path)):
            if path[i] == '':
                continue
            new_node = DirNode(path[i])
            self.last_path[i - 1].sub_nodes.append(new_node)
            self.last_path = self.last_path[:i] + [new_node]

    def print_item(self, node, prefix, indent='\t', sep='\\'):
        print(prefix, node.name, sep=sep)
        for s in node.sub_nodes:
            self.print_item(s, prefix + sep + node.name, node.name, sep)

    def show(self):
        for node in self.root:
            self.print_item(node, '', '')

    def parse_path(self, longpath):
        paths = longpath.split('\n')
        for path in paths:
            self.add_item(path)
