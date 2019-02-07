from snippet.find import *


class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == dp[-1]:
                continue
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            j = find_first_of(dp, nums[i])
            if dp[j] == nums[i]:
                continue
            dp[j] = nums[i]
        return len(dp)

    def lengthOfLIS2(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        counter = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and counter[j] + 1 > counter[i]:
                    counter[i] = counter[j] + 1
        return max(counter)


def test_lengthOfLIS():
    x = [10, 9, 2, 5, 3, 7, 101, 18]
    y = 4
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS2():
    x = [1, 2, 3]
    y = 3
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS3():
    x = [4, 1, 3, 2, 1, 3]
    y = 3
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS4():
    x = []
    y = 0
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS5():
    x = [1]
    y = 1
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS6():
    x = [1, 2]
    y = 2
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS7():
    x = [2, 1]
    y = 1
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS8():
    x = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    y = 6
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS9():
    x = [2, 2]
    y = 1
    assert (Solution().lengthOfLIS(x) == y)


def test_lengthOfLIS10():
    x = [4, 10, 4, 3, 8, 9]
    y = 3
    assert (Solution().lengthOfLIS(x) == y)
