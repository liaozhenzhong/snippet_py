class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in reversed(range(len(shifts) - 1)):
            shifts[i] += shifts[i + 1]
        shifts = [i % 26 for i in shifts]
        res = ''.join([chr((ord(c) - ord('a') + i) % 26 + ord('a'))
                       for c, i in zip(S, shifts)])
        return res


def test_shift():
    S = "abc"
    shifts = [3, 5, 9]
    r = Solution().shiftingLetters(S, shifts)
    assert(r == "rpl")

    S = 'ab'
    shifts = [27, 26]
    assert(Solution().shiftingLetters(S, shifts) == 'bb')

    S = ''
    shifts = []
    assert(Solution().shiftingLetters(S, shifts) == '')

    S = 'a'
    shifts = [1]
    assert(Solution().shiftingLetters(S, shifts) == 'b')
