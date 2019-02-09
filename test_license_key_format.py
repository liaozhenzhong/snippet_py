class Solution:
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        string_no_dash = ''.join([c.upper() for c in S if c != '-'])
        remainder = len(string_no_dash) % K
        ans = [string_no_dash[:remainder], '-'] if remainder > 0 else []
        for i in range(remainder, len(string_no_dash), K):
            ans.append(string_no_dash[i:i + K])
            ans.append('-')
        if ans and ans[-1] == '-':
            ans.pop()
        return ''.join(ans)


def test_licenseKeyFormatting():
    S = "5F3Z-2e-9-w"
    K = 4
    Out = "5F3Z-2E9W"
    assert(Solution().licenseKeyFormatting(S, K) == Out)


def test_licenseKeyFormatting_2():
    S = "5F3Z-2e-9-w6"
    K = 4
    Out = "5-F3Z2-E9W6"
    assert(Solution().licenseKeyFormatting(S, K) == Out)


def test_licenseKeyFormatting_3():
    S = "9-w6"
    K = 4
    Out = "9W6"
    assert(Solution().licenseKeyFormatting(S, K) == Out)


def test_licenseKeyFormatting_4():
    S = ""
    K = 4
    Out = ""
    assert(Solution().licenseKeyFormatting(S, K) == Out)
