class Solution:
    def bestRotation(self, A):
        N = len(A)
        B = [0] * N
        for i, x in enumerate(A):
            if x > i:
                j = i + 1
                B[j] += 1

                j = i + 1 + N - x
                if j < N:
                    B[j] -= 1

            else:
                j = 0
                B[j] += 1

                j = i - x + 1
                if j < N:
                    B[j] -= 1

                j = i + 1
                if j < N:
                    B[j] += 1

        for i in range(1, N):
            B[i] += B[i - 1]
        C = max(B)
        for i in range(N):
            if B[i] == C:
                return i

    def bestRotation2(self, A):
        L = len(A)
        A = A * 2
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
    assert (Solution().bestRotation(X) == 3)


def test_best_rotation_2():
    X = [0, 1, 2]
    assert (Solution().bestRotation(X) == 0)


def test_best_rotation_3():
    X = [3, 0, 1, 2]
    assert (Solution().bestRotation(X) == 1)


def test_best_rotation_4():
    X = [1, 3, 0, 2, 4]
    assert (Solution().bestRotation(X) == 0)


def test_best_rotation_5():
    X = [6, 2, 8, 3, 5, 2, 4, 3, 7, 6]
    assert (Solution().bestRotation(X) == 9)
