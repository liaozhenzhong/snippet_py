class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        vs = [c for c in s]
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vow_pos = [i for i, v in enumerate(vs) if v in vowels]
        t = len(vow_pos) // 2 + 1
        for i, j in zip(vow_pos[:t], vow_pos[-1:-t:-1]):
            vs[i], vs[j] = vs[j], vs[i]
        return ''.join(vs)


def test_reverse():
    assert (Solution().reverseVowels("leetcode") == "leotcede")


def test_reverse2():
    assert (Solution().reverseVowels("hello") == "holle")


def test_reverse3():
    assert (Solution().reverseVowels("0aeoiou9") == "0uoioea9")


def test_reverse4():
    assert (Solution().reverseVowels("") == "")


def test_reverse5():
    assert (Solution().reverseVowels("a") == "a")


def test_reverse6():
    assert (Solution().reverseVowels("l") == "l")


def test_reverse7():
    assert (Solution().reverseVowels("aA") == "Aa")
