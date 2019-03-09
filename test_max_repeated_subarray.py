class Solution:
    def findLength(self, A, B):
        match = [[0]*len(A) for _ in range(len(B))]
        for i in range(len(A)):
            if A[i] == B[0]:
                match[0][i] = 1
        for i in range(len(B)):
            if A[0] == B[i]:
                match[i][0] = 1
        for i in range(1, len(B)):
            for j in range(1, len(A)):
                if A[j] == B[i]:
                    match[i][j] = match[i-1][j-1] + 1
        return max([max(row) for row in match])

def test_find_length():
    assert Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3

def test_find_length_1():
    assert Solution().findLength([1, 2, 4, 6, 7, 8, 2, 1], [4, 6, 7, 8, 5, 5]) == 4

def test_find_length_2():
    assert Solution().findLength([4, 6, 7, 8, 2, 1], [5, 5, 4, 6, 7, 8, 5, 5]) == 4

def test_find_length_3():
    assert Solution().findLength([1], [1]) == 1

def test_find_length_3():
    assert Solution().findLength([0], [1]) == 0
