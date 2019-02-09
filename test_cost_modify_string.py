class Solution(object):
    def cost_modify_string(self, s, t):
        if not s:
            return len(t)
        if not t:
            return len(s)

        c = [[0] * len(s) for _ in range(len(t))]
        c[0][0] = 1 if s[0] != t[0] else 0
        for i in range(1, len(s)):
            c[0][i] = c[0][i - 1] if s[i] == t[0] else (c[0][i - 1] + 1)
        for i in range(1, len(t)):
            c[i][0] = c[i - 1][0] if t[i] == s[0] else (c[i - 1][0] + 1)
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if t[i] == s[j]:
                    c[i][j] = min(c[i - 1][j - 1], c[i - 1]
                                  [j] + 1, c[i][j - 1] + 1)
                else:
                    c[i][j] = min(c[i - 1][j - 1] + 1, c[i - 1]
                                  [j] + 1, c[i][j - 1] + 1)

        return c[-1][-1]


def test_cost_modify_string():
    s = 'sitting'
    t = 'kitten'
    assert(Solution().cost_modify_string(s, t) == 3)


def test_cost_modify_string_2():
    s = 'adc'
    t = 'abc'
    assert(Solution().cost_modify_string(s, t) == 1)


def test_cost_modify_string_3():
    s = ''
    t = ''
    assert(Solution().cost_modify_string(s, t) == 0)


def test_cost_modify_string_4():
    s = 'ac'
    t = 'abc'
    assert(Solution().cost_modify_string(s, t) == 1)


def test_cost_modify_string_5():
    s = 'acd'
    t = 'abc'
    assert(Solution().cost_modify_string(s, t) == 2)


def test_cost_modify_string_6():
    s = ''
    t = 'abc'
    assert(Solution().cost_modify_string(s, t) == 3)


def test_cost_modify_string_7():
    s = 'abc'
    t = ''
    assert(Solution().cost_modify_string(s, t) == 3)


def test_cost_modify_string_8():
    s = 'abc'
    t = 'abc'
    assert(Solution().cost_modify_string(s, t) == 0)
