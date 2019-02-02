class Solution:
    def minDeletionSize(self, A):
        if not A:
            return 0

        need_care = [True] * len(A)
        need_care[0] = False
        res = 0
        for j in range(len(A[0])):
            col_to_del = False
            for i in range(1, len(A)):
                if need_care[i] and A[i - 1][j] > A[i][j]:
                    col_to_del = True
                    break
            if col_to_del:
                res += 1
            else:
                for i in range(1, len(A)):
                    if A[i - 1][j] < A[i][j]:
                        need_care[i] = False
        return res


def test_min_del_size():
    X = ["ca", "bb", "ac"]
    res = Solution().minDeletionSize(X)
    assert res == 1


def test_min_del_size_2():
    X = ["xc", "yb", "za"]
    res = Solution().minDeletionSize(X)
    assert res == 0

def test_min_del_size_3():
    X = ["zyx","wvu","tsr"]
    res = Solution().minDeletionSize(X)
    assert res == 3

def test_min_del_size_4():
    X = []
    res = Solution().minDeletionSize(X)
    assert res == 0