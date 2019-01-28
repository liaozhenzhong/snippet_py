from random import randint
from snippet.k_most import *

def test_k_largest():
    X = [randint(1, 20) for _ in range(10)]
    k = randint(0, 9)
    Y = sorted(X, reverse=True)
    assert(k_largest(X, k) == Y[:k])

def test_k_largest_k_0():
    X = [randint(1, 20) for _ in range(10)]
    k = 0
    Y = sorted(X, reverse=True)
    assert(k_largest(X, k) == Y[:k])

def test_k_largest_empty():
    X = []
    k = 3
    Y = [-inf, -inf, -inf]
    assert(k_largest(X, k) == Y[:k])
