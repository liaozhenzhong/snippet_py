class Solution:
    def maximalSquare(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0

        if not any([any(i) for i in matrix]):
            return 0

        H = len(matrix)
        W = len(matrix[0])

        for i in range(H):
            for j in range(W):
                matrix[i][j] = 0 if matrix[i][j] == "0" else 1

        up_spaces = [[0] * W for _ in range(H)]
        left_spaces = [[0] * W for _ in range(H)]
        square_len = [[0] * W for _ in range(H)]

        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    continue
                up_spaces[i][j] = up_spaces[i - 1][j] + 1
                left_spaces[i][j] = left_spaces[i][j - 1] + 1
                square_len[i][j] = 1

        for i in range(1, H):
            for j in range(1, W):
                if matrix[i][j] == 0:
                    continue
                square_len[i][j] = min(
                    square_len[i - 1][j - 1], up_spaces[i - 1][j], left_spaces[i][j - 1]) + 1

        return max([max(i) for i in square_len])


def test_square():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]
    res = Solution().maximalSquare(x)
    assert res == 2


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
    assert res == 2


def test_square4():
    x = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
    ]
    res = Solution().maximalSquare(x)
    assert res == 3


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


def test_square8():
    x = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
        "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

    res = Solution().maximalSquare(x)
    assert res == 4
