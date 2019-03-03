from math import inf

class Solution:
    def find_first_island_cell(self, A):
        H = len(A)
        W = len(A[0])
        for i in range(H):
            for j in range(W):
                if A[i][j] == 0:
                    continue
                return i, j

    def in_the_map(self, i, j, H, W):
        return -1 < i and -1 < j and i < H and j < W

    def find_one_island(self, A):
        H = len(A)
        W = len(A[0])

        i, j = self.find_first_island_cell(A)

        island = {(i, j)}
        to_visit = {(i, j)}

        while to_visit:
            i, j = to_visit.pop()

            for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if not self.in_the_map(a, b, H, W):
                    continue
                if A[a][b] == 0:
                    continue
                if (a, b) not in island:
                    island.add((a, b))
                    if (a, b) not in to_visit:
                        to_visit.add((a, b))

        return island

    def find_another_island(self, A, island):
        H = len(A)
        W = len(A[0])

        island2 = set()
        for i in range(H):
            for j in range(W):
                if A[i][j] == 0:
                    continue

                if (i, j) in island:
                    continue

                island2.add((i, j))

        return island2


    def shortestBridge(self, A: 'List[List[int]]') -> 'int':
        if not A or not A[0]:
            return

        island = self.find_one_island(A)

        H = len(A)
        W = len(A[0])

        shortest_map = [[inf for _ in range(W)] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if (i, j) in island:
                    shortest_map[i][j] = 0
                    continue
                if i > 0:
                    shortest_map[i][j] = min(shortest_map[i-1][j] + 1, shortest_map[i][j])
                if j > 0:
                    shortest_map[i][j] = min(shortest_map[i][j-1] + 1, shortest_map[i][j])
        for i in reversed(range(H)):
            for j in reversed(range(W)):
                if (i, j) in island:
                    shortest_map[i][j] = 0
                    continue
                if i < H-1:
                    shortest_map[i][j] = min(shortest_map[i+1][j] + 1, shortest_map[i][j])
                if j < W-1:
                    shortest_map[i][j] = min(shortest_map[i][j+1] + 1, shortest_map[i][j])

        island2 = self.find_another_island(A, island)

        shortest_jump = inf
        for i, j in island2:
            if shortest_map[i][j] < shortest_jump:
                shortest_jump = shortest_map[i][j]

        return shortest_jump-1

def test_shortest_bridge():
    A = [[0,1],[1,0]]
    assert Solution().shortestBridge(A) == 1

def test_shortest_bridge2():
    A = [[0,1,0],[0,0,0],[0,0,1]]
    assert Solution().shortestBridge(A) == 2

def test_shortest_bridge3():
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    assert Solution().shortestBridge(A) == 1

