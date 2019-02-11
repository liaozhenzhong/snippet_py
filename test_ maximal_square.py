import copy


class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        H = len(matrix)
        W = len(matrix[0])

        # for i in range(H):
        #     for j in range(W):
        #         matrix[i][j] = 0 if matrix[i][j] == '0' else 1

        up = copy.deepcopy(matrix)
        left = copy.deepcopy(matrix)
        square = copy.deepcopy(matrix)

        for i in range(1, H):
            for j in range(W):
                if matrix[i][j] == 0:
                    continue
                up[i][j] = up[i-1][j] + 1

        for i in range(H):
            for j in range(1, W):
                if matrix[i][j] == 0:
                    continue
                left[i][j] = left[i][j-1] + 1

        for i in range(1, H):
            for j in range(1, W):
                if matrix[i][j] == 0:
                    continue
                square[i][j] = min(square[i-1][j-1],
                                   up[i-1][j], left[i][j-1]) + 1

        return max([max(i) for i in square])**2


def test_square():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 4


def test_square2():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 1


def test_square3():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 4


def test_square4():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
    ]
    res = Solution().maximalSquare(x)
    assert res == 9


def test_square5():
    x = [
        [0, 0],
        [0, 0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 0


def test_square6():
    x = [
    ]
    res = Solution().maximalSquare(x)
    assert res == 0


def test_square7():
    x = [
        [0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 0
