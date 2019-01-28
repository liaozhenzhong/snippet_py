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
        self.E = E
        self.V = V
        self.time = 0

    def show(self):
        print([v for v in self.V.values()])

    def tick(self):
        self.time += 1
        return self.time

    def dfs_init(self):
        self.time = 0
        for v in self.V.values():
            v.seen = False
            v.finish = None
            v.prev = None

    def dfs(self, s):
        yield self.V[s]
        self.V[s].seen = True
        for nei in self.E[s]:
            if not self.V[nei].seen:
                self.V[nei].prev = s
                yield from self.dfs(nei)
        self.V[s].finish = self.tick()

    def bfs_init(self):
        for v in self.V.values():
            v.seen = False
            v.degree = 0
            v.prev = None
            v.weight = math.inf

    def bfs(self, s):
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
        for k in self.V:
            if not self.V[k].seen:
                [_ for _ in self.dfs(k)]
        order = sorted([(v.finish, v.key) for v in self.V.values()], reverse=True)
        order = [v[1] for v in order]
        return order

    def relax(self, u, v, weight):
        if u.weight + weight < v.weight:
            v.weight = u.weight + weight

    def dijkstra_init(self):
        for v in self.V:
            self.V[v].weight = math.inf

    def dijkstra(self, s, t):
        Q = list(self.V.values())
        self.V[s].weight = 0
        
        while Q:
            heapq.heapify(Q)
            u = heapq.heappop(Q)
            for v, weight in self.E[u.key].items():
                self.relax(u, self.V[v], weight)
        
        return self.V[t].weight

    def dijkstra_edge_list_format(self, s, t):
        Q = list(self.V.values())
        self.V[s].weight = 0
        
        while Q:
            heapq.heapify(Q)
            u = heapq.heappop(Q)
            for v, weight in self.E[u.key]:
                self.relax(u, self.V[v], weight)
        
        return self.V[t].weight
