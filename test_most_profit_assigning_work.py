from math import inf

def find_last_of(X, k):
    Z = [-inf] + X + [inf]
    i = len(Z)//2
    step = len(Z)//4
    while True:
        if Z[i] <= k and Z[i+1] > k:
            return i - 1
        elif Z[i+1] <= k:
            i += step
        else:
            i -= step
        step = max(step//2, 1)


class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        db = dict()
        for d, p in zip(difficulty, profit):
            if d not in db or p > db[d]:
                db[d] = p

        keys = list(db.keys())

        res = 0
        for w in worker:
            i = find_last_of(keys, w)
            if i < 0:
                continue
            res += db[keys[i]]

        return res



def test_max_profit():
    assert(Solution().maxProfitAssignment(
        [2,4,6,8,10], 
        [10,20,30,40,50], 
        [4,5,6,7]
        ) == 100)

def test_max_profit_2():
    assert(Solution().maxProfitAssignment(
        [85,47,57],
        [24,66,99],
        [40,25,25],
        ) == 0)

def test_max_profit_3():
    assert(Solution().maxProfitAssignment(
        [68,35,52,47,86],
        [67,17,1,81,3],
        [92,10,85,84,82],
        ) == 324)
