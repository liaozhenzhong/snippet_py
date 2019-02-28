from collections import deque

class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        strK = []
        while K > 0:
            strK.append(K % 10)
            K = K // 10
        A.reverse()
        is_more_than_10 = 0
        res = []
        for i, j in zip(A, strK):
            tmp = int(i) + int(j) + is_more_than_10
            res.append(tmp%10)
            is_more_than_10 = 0 if tmp < 10 else 1

        longer_str = A if len(A) > len(strK) else strK
        short_str = A if len(A) <= len(strK) else strK
        for i in range(len(short_str), len(longer_str)):
            tmp = int(longer_str[i]) + is_more_than_10
            res.append(tmp%10)
            is_more_than_10 = 0 if tmp < 10 else 1

        if is_more_than_10:
            res.append(1)

        res.reverse()
        return res


    def addToArrayForm2(self, A: 'List[int]', K: 'int') -> 'List[int]':
        AA = 0
        L = len(A)
        for i in reversed(range(len(A))):
            AA += A[i]*(10**(L-i-1))
        AA += K
        res = deque()
        while AA // 10:
            res.appendleft(AA%10)
            AA = AA // 10
        if AA:
            res.appendleft(AA)
        if not res:
            res = [0]
        return list(res)


def test_add_to_array_form():
    A = [1,2,0,0]
    K = 34
    assert Solution().addToArrayForm(A, K) == [1,2,3,4]

def test_add_to_array_form1():
    A = [2, 7, 4]
    K = 181
    assert Solution().addToArrayForm(A, K) == [4, 5, 5]

def test_add_to_array_form2():
    A = [2, 1, 5]
    K = 806
    assert Solution().addToArrayForm(A, K) == [1,0,2,1]

def test_add_to_array_form3():
    A = [0]
    K = 0
    assert Solution().addToArrayForm(A, K) == [0]

test_add_to_array_form3()
