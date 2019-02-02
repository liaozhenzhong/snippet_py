class Solution:
    def rob(self, nums):
        R = 0
        N = 0
        for i in nums:
            R1 = i + N
            N1 = max(R, N)
            R, N = R1, N1
        return max(R, N)


def test_robber():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_robber2():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12


def test_robber3():
    assert Solution().rob([1]) == 1


def test_robber4():
    assert Solution().rob([]) == 0
