import math
from collections import deque
import heapq

class Node(object):
    def __init__(self, key):
        self.key = key
        self.seen = False
        self.finish = None
        self.degree = 0
        self.prev = None
        self.weight = math.inf

    def __repr__(self):
        return 'key:{}, \tseen:{}, \tfsh:{}, \tprev:{}, \tdeg:{}, \tweight:{}\n'.format(self.key, 
                self.seen if self.seen else 'None', 
                self.finish if self.finish is not None else 'None', 
                self.prev if self.prev is not None else 'None',
                self.degree if self.degree is not None else 'None',
                self.weight,
                )

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

class Graph(object):
    def __init__(self, E, V):
        """
        E: edges. Dict. k:{nei1, nei2}
        V: nodes. Dict. k:Node(k)
        """
        self.E = E
        self.V = V
        self.time = 0

    def show(self):
        """
        print all nodes in self.V
        """
        print([v for v in self.V.values()])

    def show_path(self, s, t):
        """
        show path from key s or key t
        s: start key
        t: finish key
        return path list of keys
        """
        path = [t]
        while self.V[t].prev:
            t = self.V[t].prev
            path.append(t)
            if t == s:
                break
        path.reverse()
        return path

    def _tick(self):
        self.time += 1
        return self.time

    def dfs_init(self):
        self.time = 0
        for v in self.V.values():
            v.seen = False
            v.finish = None
            v.prev = None

    def dfs(self, s):
        """
        depth first search in generator form.
        call dfs_init first.
        s: start key
        return nothing
        """
        yield self.V[s]
        self.V[s].seen = True
        for nei in self.E[s]:
            if not self.V[nei].seen:
                self.V[nei].prev = s
                yield from self.dfs(nei)
        self.V[s].finish = self._tick()

    def bfs_init(self):
        for v in self.V.values():
            v.seen = False
            v.degree = 0
            v.prev = None
            v.weight = math.inf

    def bfs(self, s):
        """
        breath first search in generator form.
        call bfs_init first.
        s: start key
        return nothing
        """
        q = deque()
        q.append(s)
        self.V[s].seen = True
        self.V[s].degree = 0
        while q:
            x = q.popleft()
            yield self.V[x]
            for nei in self.E[x]:
                if not self.V[nei].seen:
                    q.append(nei)
                    self.V[nei].seen = True
                    self.V[nei].prev = x
                    self.V[nei].degree = self.V[x].degree + 1

    def topo_sorted_order(self):
        """
        topological sort
        call dfs_init first
        return a list of key
        """
        for k in self.V:
            if not self.V[k].seen:
                [_ for _ in self.dfs(k)]
        order = sorted([(v.finish, v.key) for v in self.V.values()], reverse=True)
        order = [v[1] for v in order]
        return order

    def _relax(self, u, v, weight):
        if u.weight + weight < v.weight:
            v.weight = u.weight + weight

    def dijkstra_init(self):
        for v in self.V:
            self.V[v].weight = math.inf

    def dijkstra(self, s, t):
        """
        single source shortest path
        s: start key
        t: finish key
        return the weight of t
        """
        Q = list(self.V.values())
        self.V[s].weight = 0
        
        while Q:
            heapq.heapify(Q)
            u = heapq.heappop(Q)
            for v, weight in self.E[u.key].items():
                self._relax(u, self.V[v], weight)
        
        return self.V[t].weight

    def dijkstra_edge_list_format(self, s, t):
        """
        single source shortest path(format 2)
        neibhgours are stored in list, instead of dict.
        s: start key
        t: finish key
        return the weight of t
        """
        Q = list(self.V.values())
        self.V[s].weight = 0
        
        while Q:
            heapq.heapify(Q)
            u = heapq.heappop(Q)
            for v, weight in self.E[u.key]:
                self._relax(u, self.V[v], weight)
        
        return self.V[t].weight

    def longest_path_in_graph(self):
        """
        find the longest path in a graph.
        can not handle cycles.
        return the path list of keys.
        """
        self.dfs_init()
        order = self.topo_sorted_order()
        self.bfs_init()
        self.V[order[0]].degree = 0
        for u in order:
            for v in self.E[u]:
                new_degree = self.V[u].degree + 1
                if new_degree > self.V[v].degree:
                    self.V[v].degree = new_degree
                    self.V[v].prev = u

        longest_paths = []
        used_node = set()
        self.dfs_init()
        for n in order:
            if n in used_node:
                continue
            path = []
            for i in self.dfs(n):
                path.append(i.key)
                used_node.add(i.key)
            if len(path) > len(longest_paths):
                longest_paths = list(path)
        path = self.show_path(longest_paths[0], longest_paths[-1])
        path.reverse()
        return path
