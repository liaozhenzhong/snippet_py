from math import inf


def prime_factor(x):
    res = []
    end = x // 2 + 1
    for i in range(2, end):
        while x % i == 0:
            res.append(i)
            x //= i
    return res if res else [x]


class Solution:
    def mirrorReflection(self, p: 'int', q: 'int') -> 'int':
        p = prime_factor(p) + [inf]
        q = prime_factor(q) + [inf]
        i = j = 0
        P = Q = 1
        while i < len(p) and j < len(q):
            if p[i] == q[j]:
                i += 1
                j += 1
                continue
            if p[i] < q[j]:
                P *= p[i]
                i += 1
            else:
                Q *= q[j]
                j += 1

        if P % 2 == 1:
            return Q % 2
        else:
            return 3 if Q % 2 == 0 else 2


def test_mirrorReflection():
    assert(Solution().mirrorReflection(2, 1) == 2)

def test_mirrorReflection_2():
    assert(Solution().mirrorReflection(3, 1) == 1)

def test_mirrorReflection_3():
    assert(Solution().mirrorReflection(3, 2) == 0)

def test_mirrorReflection_4():
    assert(Solution().mirrorReflection(4, 1) == 2)

def test_mirrorReflection_5():
    assert(Solution().mirrorReflection(4, 3) == 2)

def test_mirrorReflection_6():
    assert(Solution().mirrorReflection(3, 4) == 0)

def test_mirrorReflection_7():
    assert(Solution().mirrorReflection(3, 5) == 1)

def test_mirrorReflection_8():
    assert(Solution().mirrorReflection(1, 1) == 1)
