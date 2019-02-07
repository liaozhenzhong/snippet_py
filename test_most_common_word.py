from collections import Counter
import string


class Solution:
    def mostCommonWord(self, paragraph: 'str', banned: 'List[str]') -> 'str':
        paragraph = paragraph.lower()
        tmp = []
        for s in paragraph:
            tmp.append(' ' if s in string.punctuation else s)
        paragraph = ''.join(tmp)
        words = paragraph.split(' ')
        c = Counter(words)
        if '' in c:
            del c['']
        for ban_word in banned:
            del c[ban_word]
        return c.most_common(1)[0][0]


def test_most_common_word():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    assert Solution().mostCommonWord(paragraph, banned) == "ball"


def test_most_common_word2():
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    assert Solution().mostCommonWord(paragraph, banned) == "b"


def test_most_common_word3():
    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    assert Solution().mostCommonWord(paragraph, banned) == "ball"
