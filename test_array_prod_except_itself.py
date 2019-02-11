class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (len(nums)) < 2:
            return None
        left = list(nums)
        right = list(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in reversed(range(len(nums) - 1)):
            right[i] = nums[i] * right[i + 1]
        res = [0] * len(nums)
        for i in range(1, len(nums) - 1):
            res[i] = left[i - 1] * right[i + 1]
        res[0] = right[1]
        res[-1] = left[-2]
        return res


def test_array_prod_except_itself():
    X = [1, 2, 3, 4]
    Y = [24, 12, 8, 6]
    assert(Solution().productExceptSelf(X) == Y)

    X = [2, 3]
    Y = [3, 2]
    assert(Solution().productExceptSelf(X) == Y)
