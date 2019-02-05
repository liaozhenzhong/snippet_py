class Solution:
    def match(self, a, b):
        if a == '(' and b == ')':
            return True
        if a == '[' and b == ']':
            return True
        if a == '{' and b == '}':
            return True
        return False

    def check_brackets(self, s):
        stk = []
        left = ['(', '[', '{']
        left = set(left)
        for c in s:
            if c in left:
                stk.append(c)
            else:
                if not stk:
                    return False
                elif not self.match(stk[-1], c):
                    return False
                else:
                    stk.pop()
        if not stk:
            return True
        return False


def test_check_brackets():
    assert(Solution().check_brackets('([])[]({})'))


def test_check_brackets2():
    assert(not Solution().check_brackets('([)]'))


def test_check_brackets3():
    assert(not Solution().check_brackets('((()'))
