# def index(self, length, i):
#     if i < 0:
#         return i + length
#     elif i >= length:
#         return i - length
#     else:
#         return i

# def findMin(self, nums: 'List[int]') -> 'int':
#     num_len = len(nums)
#     if num_len == 0:
#         return None
#     elif num_len == 1:
#         return nums[0]
#     elif num_len == 2:
#         return min(nums)

#     steps = num_len//2
#     i = 0
#     while True:
#         i1 = self.index(num_len, i)
#         i2 = self.index(num_len, i+1)
#         if nums[i1] > nums[i2]:
#             return nums[i2]
#         else:
#             i -= max(steps, 1)
#             print(i, steps)
#             steps = steps // 2


class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if not nums:
            return None
        l = 0
        r = len(nums) - 1
        while True:
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] > nums[l] and nums[l] > nums[r]:
                l = m
                continue
            elif nums[l] > nums[r] and nums[r] > nums[m]:
                r = m
                continue
            elif nums[l] < nums[m] and nums[m] < nums[r]:
                return nums[l]
            elif r - l < 3:
                return min(nums[l:r + 1])


def test_findMin():
    assert(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)


def test_findMin_2():
    assert(Solution().findMin(
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2]) == 0)


def test_findMin_3():
    assert(Solution().findMin([4, 5, 2]) == 2)


def test_findMin_4():
    assert(Solution().findMin([4, 5]) == 4)


def test_findMin_5():
    assert(Solution().findMin([4]) == 4)


def test_findMin_6():
    assert(Solution().findMin([]) is None)


def test_findMin_7():
    assert(Solution().findMin([1, 2, 3]) == 1)


def test_findMin_8():
    SPLIT = 5000
    x = [i for i in range(SPLIT, 100_000)] + [i for i in range(0, SPLIT)]
    assert(Solution().findMin(x) == 0)


def test_findMin_9():
    assert(Solution().findMin([1, 2, 3, 4, 5]) == 1)
