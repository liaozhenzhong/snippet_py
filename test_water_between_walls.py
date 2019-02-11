class Solution(object):
    def water_between_walls(self, walls):
        left = [0] * len(walls)
        right = [0] * len(walls)
        for i in range(1, len(left)):
            left[i] = max(left[i - 1], walls[i - 1])
        for i in reversed(range(len(right) - 1)):
            right[i] = max(right[i + 1], walls[i + 1])
        water = []
        for i in range(1, len(walls) - 1):
            water.append(max(0, min(left[i], right[i]) - walls[i]))
        return sum(water)


def test_water_between_walls():
    walls = [3, 0, 1, 3, 0, 5]
    assert(Solution().water_between_walls(walls) == 8)


def test_water_between_walls_2():
    walls = [0, 1, 2]
    assert(Solution().water_between_walls(walls) == 0)


def test_water_between_walls_3():
    walls = [0, 1, 1]
    assert(Solution().water_between_walls(walls) == 0)


def test_water_between_walls_4():
    walls = [0, 1, 0]
    assert(Solution().water_between_walls(walls) == 0)


def test_water_between_walls_5():
    walls = [3, 2, 1]
    assert(Solution().water_between_walls(walls) == 0)


def test_water_between_walls_6():
    walls = [1, 1, 1]
    assert(Solution().water_between_walls(walls) == 0)


def test_water_between_walls_7():
    walls = [10, 0, 5]
    assert(Solution().water_between_walls(walls) == 5)
