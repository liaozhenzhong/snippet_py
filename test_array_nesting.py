class Solution:
    def arrayNesting(self, nums):
        used = set()
        max_len = 0
        l = 0
        for i in nums:
            while i not in used:
                used.add(i)
                l += 1
                i = nums[i]
            if l > max_len:
                max_len = l
            l = 0
        return max_len


def test_nesting():
    A = [5, 4, 0, 3, 1, 6, 2]
    Z = 4
    assert Solution().arrayNesting(A) == Z


def test_nesting_2():
    A = [0, 2, 1]
    Z = 2
    assert Solution().arrayNesting(A) == Z


def test_nesting_3():
    with open('1.txt') as f:
        A = f.readline().split(',')
        A = [int(i) for i in A]
    Z = 2
    print(Solution().arrayNesting(A))


def test_nesting_4():
    A = []
    Z = 0
    assert Solution().arrayNesting(A) == Z


def test_nesting_5():
    A = [0, 1, 2]
    Z = 1
    assert Solution().arrayNesting(A) == Z
