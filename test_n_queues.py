import copy
from pprint import pprint
import time

class Solution:
    def __init__(self):
        self.sol = set()

    def print_board(self, n, records):
        res = []
        board = [['.']*n for _ in range(n)]
        for i, j in records:
            board[i][j] = 'Q'
        for row in board:
            res.append(''.join(row))
        return res

    def is_diag(self, i, j, records):
        for x, y in records:
            if abs(x - i) == abs(y - j):
                return True
        return False

    def try_step(self, n, q, records):
        if q == 0:
            self.sol.add(tuple(sorted(records)))
            return

        used_col = [i for _, i in records]

        for k in range(n):
            if k in used_col or self.is_diag(n-q, k, records):
                continue
            self.try_step(n, q - 1, records + [(n-q, k)])


    def solveNQueens(self, n):
        records = []
        self.try_step(n, n, records)
        res = []
        for sol in self.sol:
            res.append(self.print_board(n, sol))
        return res

start = time.time()
pprint(Solution().solveNQueens(8))
print(time.time() - start)
