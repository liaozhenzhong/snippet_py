class Solution:
    def uniquePaths(self, m, n):
        a, b = (m, n) if m < n else (n, m)
        a -= 1
        b -= 1
        c = a + b
        d = 1
        for i in range(a):
            d *= (c - i)
        e = 1
        for i in range(1, a+1):
            e *= i
        return d/e


def test_unique_path():
    assert Solution().uniquePaths(3, 2) == 3
    assert Solution().uniquePaths(7, 3) == 28
    assert Solution().uniquePaths(2, 2) == 2

test_unique_path()

