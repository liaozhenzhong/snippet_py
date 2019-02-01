from snippet.find import *

def test_find_first():
    X = [0, 1, 2, 3, 3, 4]
    assert(find_first_of(X, -1) == 0)
    assert(find_first_of(X, -0.5) == 0)
    assert(find_first_of(X, 0) == 0)
    assert(find_first_of(X, 0.5) == 1)
    assert(find_first_of(X, 1) == 1)
    assert(find_first_of(X, 3) == 3)
    assert(find_first_of(X, 4) == 5)
    assert(find_first_of(X, 4.5) == 6)


def test_find_last():
    X = [0, 1, 2, 3, 4, 5]
    assert(find_last_of(X, 2.5) == 2)
    assert(find_last_of(X, -1) == -1)
    assert(find_last_of(X, 0) == 0)
    assert(find_last_of(X, 0.5) == 0)
    assert(find_last_of(X, 3) == 3)
    assert(find_last_of(X, 5) == 5)
    assert(find_last_of(X, 6) == 5)
