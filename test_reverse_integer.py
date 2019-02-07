class Solution:
    def reverse(self, x: 'int') -> 'int':
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        y = 0
        while x > 0:
            y *= 10
            y += x%10
            x //= 10
        res = y*sign
        
        if res > (2**31 - 1):
            return 0
        if res < -2**31:
            return 0
        return res

def test_reverse():
    assert(Solution().reverse(-123) == -321)

def test_reverse_2():
    assert(Solution().reverse(123) == 321)

def test_reverse_3():
    assert(Solution().reverse(0) == 0)

def test_reverse_4():
    assert(Solution().reverse(1) == 1)

def test_reverse_5():
    assert(Solution().reverse(14) == 41)
