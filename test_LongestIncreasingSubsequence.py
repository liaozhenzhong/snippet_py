from math import inf

class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        H = W = len(nums) + 1
        match = [[0]*W for _ in range(H)]
        the_max = -1
        nums.insert(0, inf)
        for i in range(1, H):
            for j in range(1, W):
                if nums[i] < nums[j] and nums[j-1] < nums[j]:
                    match[i][j] = match[i-1][j-1] + 1
                    if match[i][j] > the_max:
                        the_max = match[i][j]
                else:
                    match[i][j] = max(match[i][j-1], match[i-1][j])
        return the_max + 1


def test_lengthOfLIS():
    x = [10,9,2,5,3,7,101,18]
    y = 4
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS2():
    x = [1, 2, 3]
    y = 3
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS3():
    x = [4, 1, 3, 2, 1, 3]
    y = 3
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS4():
    x = []
    y = 0
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS5():
    x = [1]
    y = 1
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS6():
    x = [1, 2]
    y = 2
    assert(Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS7():
    x = [2, 1]
    y = 0
    assert(Solution().lengthOfLIS(x) == y)