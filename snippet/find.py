from math import inf


def find_first_of(X, k):
    Z = [-inf] + X + [inf]
    i = len(Z)//2
    step = len(Z)//4
    while True:
        if Z[i-1] < k and Z[i] >= k:
            return i - 1
        elif Z[i-1] >= k:
            i -= step
        else:
            i += step
        step = max(step//2, 1)


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
