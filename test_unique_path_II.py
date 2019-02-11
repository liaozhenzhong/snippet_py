class Solution:
    def uniquePathsWithObstacles(
            self, obstacleGrid: 'List[List[int]]') -> 'int':
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        H = len(obstacleGrid)
        W = len(obstacleGrid[0])
        ways = [[0] * W for _ in range(H)]

        for i in range(W):
            if obstacleGrid[0][i] == 1:
                break
            ways[0][i] = 1

        for i in range(H):
            if obstacleGrid[i][0] == 1:
                break
            ways[i][0] = 1

        for i in range(1, H):
            for j in range(1, W):
                if obstacleGrid[i][j] == 1:
                    continue
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

        return ways[-1][-1]


def test_uniquePathsWithObstacles():
    x = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    res = Solution().uniquePathsWithObstacles(x)
    assert res == 2


def test_uniquePathsWithObstacles_2():
    x = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    res = Solution().uniquePathsWithObstacles(x)
    assert res == 3


def test_uniquePathsWithObstacles_3():
    x = [
        [0, 0],
        [0, 0],
    ]

    res = Solution().uniquePathsWithObstacles(x)
    assert res == 2


def test_uniquePathsWithObstacles_4():
    x = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    res = Solution().uniquePathsWithObstacles(x)
    assert res == 6


def test_uniquePathsWithObstacles_5():
    x = [[]]

    res = Solution().uniquePathsWithObstacles(x)
    assert res == 0


test_uniquePathsWithObstacles_5()
