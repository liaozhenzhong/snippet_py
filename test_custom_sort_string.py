class Solution:
    def customSortString(self, S: 'str', T: 'str') -> 'str':
        counter = [0] * 26
        pivit = ord('a')
        for c in T:
            counter[ord(c) - pivit] += 1
        res = []
        for c in S:
            offset = ord(c) - pivit
            res += [c] * counter[offset]
            counter[offset] = 0
        for i in range(26):
            if counter[i] > 0:
                res += [chr(i + pivit)] * counter[i]
        return ''.join(res)


def test_customSortString():
    S = "cba"
    T = "abcd"
    assert Solution().customSortString(S, T) == 'cbad'


def test_customSortString_5():
    S = "cba"
    T = "dabcdabcd"
    assert Solution().customSortString(S, T) == 'ccbbaaddd'


def test_customSortString_4():
    S = "abc"
    T = ""
    assert Solution().customSortString(S, T) == ''


def test_customSortString_3():
    S = ""
    T = ""
    assert Solution().customSortString(S, T) == ''


def test_customSortString_2():
    S = ""
    T = "abcd"
    assert Solution().customSortString(S, T) == 'abcd'
