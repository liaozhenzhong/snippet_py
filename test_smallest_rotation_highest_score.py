class Solution:
    def bestRotation(self, A):
        L = len(A)
        A = A*2
        best_points = 0
        best_k = 0
        for k in range(L):
            point = 0
            for i in range(L):
                if A[k + i] <= i:
                    point += 1
            if point > best_points:
                best_points = point
                best_k = k
        return best_k


def test_best_rotation():
    X = [2, 3, 1, 4, 0]
    assert(Solution().bestRotation(X) == 3)


def test_best_rotation_2():
    X = [0, 1, 2]
    assert(Solution().bestRotation(X) == 0)

def test_best_rotation_3():
    X = [3, 0, 1, 2]
    assert(Solution().bestRotation(X) == 1)


def test_best_rotation_4():
    X = [1, 3, 0, 2, 4]
    assert(Solution().bestRotation(X) == 0)
