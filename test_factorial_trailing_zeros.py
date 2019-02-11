from math import factorial


class Solution:
    def trailingZeroes(self, n: 'int') -> 'int':
        ans = 0
        i = 1
        while 5 ** i <= n:
            ans += n // (5 ** i)
            i += 1
        return ans

    def trailingZeroes_standard(self, n: 'int') -> 'int':
        f = factorial(n)
        i = 1
        while f % (10 ** i) == 0:
            i += 1
        return i - 1


def test_trailingZeroes():
    assert(Solution().trailingZeroes(0) == 0)
    assert(Solution().trailingZeroes(1) == 0)
    assert(Solution().trailingZeroes(2) == 0)
    assert(Solution().trailingZeroes(3) == 0)
    assert(Solution().trailingZeroes(4) == 0)
    assert(Solution().trailingZeroes(5) == 1)
    assert(Solution().trailingZeroes(6) == 1)
    assert(Solution().trailingZeroes(7) == 1)
    assert(Solution().trailingZeroes(8) == 1)
    assert(Solution().trailingZeroes(9) == 1)
    assert(Solution().trailingZeroes(10) == 2)
    assert(Solution().trailingZeroes(11) == 2)
    assert(Solution().trailingZeroes(12) == 2)
    assert(Solution().trailingZeroes(13) == 2)
    assert(Solution().trailingZeroes(14) == 2)
    assert(Solution().trailingZeroes(15) == 3)


def test_trailingZeroes_2():
    for i in range(200):
        x = Solution().trailingZeroes_standard(i)
        y = Solution().trailingZeroes(i)
        if x != y:
            print(i, x, y)
