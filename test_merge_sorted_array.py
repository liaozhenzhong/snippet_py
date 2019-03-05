from math import inf

class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        i = m - 1
        j = n - 1
        k = m + n - 1
        while -1 < k:
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1


def test_merge_array():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

def test_merge_array_1():
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == []

def test_merge_array_2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]

def test_merge_array_3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]

def test_merge_array_4():
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1, 2]
