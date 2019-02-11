import copy


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            res[i][0] = int(matrix[i][0])
        for j in range(len(matrix[0])):
            res[0][j] = int(matrix[0][j])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                res[i][j] = 1 + min(res[i - 1][j], res[i][j - 1],
                                    res[i - 1][j - 1]) if matrix[i][j] == "1" else 0
        return max(map(max, res))**2

    def maximalSquare3(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        H = len(matrix)
        W = len(matrix[0])

        for i in range(H):
            for j in range(W):
                matrix[i][j] = 0 if matrix[i][j] == '0' else 1

        up = copy.deepcopy(matrix)
        left = copy.deepcopy(matrix)
        square = copy.deepcopy(matrix)

        for i in range(1, H):
            for j in range(W):
                if matrix[i][j] == 0:
                    continue
                up[i][j] = up[i - 1][j] + 1

        for i in range(H):
            for j in range(1, W):
                if matrix[i][j] == 0:
                    continue
                left[i][j] = left[i][j - 1] + 1

        for i in range(1, H):
            for j in range(1, W):
                if matrix[i][j] == 0:
                    continue
                square[i][j] = min(square[i - 1][j - 1],
                                   up[i - 1][j], left[i][j - 1]) + 1

        return max([max(i) for i in square])**2

    def maximalSquare2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        H = len(matrix)
        W = len(matrix[0])

        for i in range(H):
            for j in range(W):
                matrix[i][j] = 0 if matrix[i][j] == '0' else 1

        info = []

        for i in range(H):
            row = []
            for j in range(W):
                t = matrix[i][j]
                row.append([t, t, t])
            info.append(row)

        largest = 0
        for i in range(H):
            for j in range(W):
                if info[i][j][2] > largest:
                    largest = info[i][j][2]
                if matrix[i][j] == 0:
                    continue
                if i > 0:
                    info[i][j][0] = info[i - 1][j][0] + 1
                if j > 0:
                    info[i][j][1] = info[i][j - 1][1] + 1
                if i > 0 and j > 0:
                    info[i][j][2] = min(info[i - 1][j - 1][2],
                                        info[i - 1][j][0], info[i][j - 1][1]) + 1
                    if info[i][j][2] > largest:
                        largest = info[i][j][2]

        return largest**2


def test_maximalSquare():
    mat = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]]
    assert Solution().maximalSquare(mat) == 4


def test_maximalSquare_2():
    mat = [
    ]
    assert Solution().maximalSquare(mat) == 0


def test_maximalSquare_3():
    mat = [
        ["0"]
    ]
    assert Solution().maximalSquare(mat) == 0


def test_maximalSquare_4():
    mat = [
        ["0", "0"],
    ]
    assert Solution().maximalSquare(mat) == 0


def test_maximalSquare_5():
    mat = [
        ["0", "0"],
        ["0", "0"],
    ]
    assert Solution().maximalSquare(mat) == 0


def test_maximalSquare_6():
    mat = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "1", "1", "1"]]
    assert Solution().maximalSquare(mat) == 9


def test_maximalSquare_7():
    mat = [
        ["1"]
    ]
    assert Solution().maximalSquare(mat) == 1


def test_maximalSquare_8():
    mat = [
        ["0", "1"],
    ]
    assert Solution().maximalSquare(mat) == 1
