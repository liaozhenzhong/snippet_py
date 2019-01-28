from snippet.kth_elem import *
from random import randrange

def test_kth_elem():
    for _ in range(1000):
        length = randrange(1, 20)
        X = [randrange(-100, 100) for _ in range(length)]
        Y = sorted(X)
        k = randrange(length)
        assert(kth_elem(X, k, 0, length) == Y[k])
