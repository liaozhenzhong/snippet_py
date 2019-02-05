class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        longest_value = (-1, -1)
        longest = -1
        for i in range(len(s)):
            tmp_len = 0
            for j in range(len(s) - i):
                if i - j < 0:
                    break
                if s[i + j] == s[i - j]:
                    if j == 0:
                        tmp_len += 1
                    else:
                        tmp_len += 2
                    if tmp_len > longest:
                        longest = tmp_len
                        longest_value = (i - j, i + j)
                else:
                    break

        for i in range(len(s)):
            tmp_len = 0
            for j in range(len(s) - i - 1):
                if i - j < 0:
                    break
                if s[i + 1 + j] == s[i - j]:
                    tmp_len += 2
                    if tmp_len > longest:
                        longest = tmp_len
                        longest_value = (i - j, i + 1 + j)
                else:
                    break

        if longest == -1:
            return ''
        return s[longest_value[0]:longest_value[1] + 1]


def test_longest():
    assert (Solution().longestPalindrome('abcbb') == 'bcb')
    assert (Solution().longestPalindrome('babad') == 'bab')
    assert (Solution().longestPalindrome('cbbd') == 'bb')
    assert (Solution().longestPalindrome('') == '')
    assert (Solution().longestPalindrome('1234321') == '1234321')
    assert (Solution().longestPalindrome('abb') == 'bb')
    assert (Solution().longestPalindrome('aacdefcaa') == 'aa')
    assert (Solution().longestPalindrome('abcd') == 'a')
    assert (Solution().longestPalindrome('a') == 'a')
