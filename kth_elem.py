def kth_elem(X, k, l, r):
    i = l
    j = l
    while j < r - 1:
        if X[j] <= X[r - 1]:
            X[i], X[j] = X[j], X[i]
            i += 1
        j += 1
    X[i], X[r - 1] = X[r - 1], X[i]
    if k == i:
        return X[i]
    elif k < i:
        return kth_elem(X, k, l, i)
    else:
        return kth_elem(X, k, i + 1, r)
