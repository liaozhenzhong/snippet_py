class Solution(object):
    def count_it(self, s):
        if not s:
            return ''

        res = []
        counter = 0
        prev = s[0]
        for c in s:
            if c == prev:
                counter += 1
            else:
                res.append('{}{}'.format(counter, prev))
                prev = c
                counter = 1
        if counter > 0:
            res.append('{}{}'.format(counter, prev))
        return ''.join(res)


def test_count_it():
    s = 'AABBBBCCCDDDDDE'
    c = '2A4B3C5D1E'
    assert(Solution().count_it(s) == c)

def test_count_it_2():
    s = 'A'
    c = '1A'
    assert(Solution().count_it(s) == c)

def test_count_it_3():
    s = ''
    c = ''
    assert(Solution().count_it(s) == c)

def test_count_it_4():
    s = 'ABAB'
    c = '1A1B1A1B'
    assert(Solution().count_it(s) == c)
