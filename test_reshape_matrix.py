class Solution:
    def gene_data(self, X):
        for i in range(len(X)):
            for j in range(len(X[0])):
                yield X[i][j]


    def matrixReshape(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        if len(nums)*len(nums[0]) != r*c:
            return nums

        g = self.gene_data(nums)
        new_mat = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = next(g)

        return new_mat


def test_reshape_matrix():
    X = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
         ]
    assert(Solution().matrixReshape(X, 3, 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


def test_reshape_matrix2():
    X = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
    ]
    assert (Solution().matrixReshape(X, 4, 4) == X)


def test_reshape_matrix3():
    X = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
    ]
    assert (Solution().matrixReshape(X, 1, 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])

def test_reshape_matrix4():
    X = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
    ]
    assert (Solution().matrixReshape(X, 0, 0) == X)


def test_reshape_matrix5():
    X = [[]]
    assert (Solution().matrixReshape(X, 3, 4) == X)