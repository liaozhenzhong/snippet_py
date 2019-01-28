from math import inf

def k_largest(X, k):
    res = [-inf]*(k + 1)
    for x in X:
        res[-1] = x
        for i in reversed(range(len(res) - 1)):
            if res[i] < res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
    return res[:-1]

def k_smallest(X, k):
    res = [inf]*(k + 1)
    for x in X:
        res[-1] = x
        for i in reversed(range(len(res) - 1)):
            if res[i] > res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
    return res[:-1]