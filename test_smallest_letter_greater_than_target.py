
def find_last_of(X, k):
    Z = ['Z'] + X + ['{']
    i = len(Z)//2
    step = len(Z)//4
    while True:
        if Z[i] <= k and Z[i+1] > k:
            return i % len(X)
        elif Z[i+1] <= k:
            i += step
        else:
            i -= step
        step = max(step//2, 1)


class Solution:
    def nextGreatestLetter(self, letters: 'List[str]', target: 'str') -> 'str':
        res = find_last_of(letters, target)
        return letters[res]


def test_nextGreatestLetter():
    letters = ["c", "f", "j"]
    target = "a"
    assert(Solution().nextGreatestLetter(letters, target) == "c")


def test_nextGreatestLetter_2():
    letters = ["c", "f", "j"]
    target = "c"
    assert(Solution().nextGreatestLetter(letters, target) == "f")


def test_nextGreatestLetter_3():
    letters = ["c", "f", "j"]
    target = "d"
    assert(Solution().nextGreatestLetter(letters, target) == "f")


def test_nextGreatestLetter_4():
    letters = ["c", "f", "j"]
    target = "g"
    assert(Solution().nextGreatestLetter(letters, target) == "j")


def test_nextGreatestLetter_5():
    letters = ["c", "f", "j"]
    target = "j"
    assert(Solution().nextGreatestLetter(letters, target) == "c")


def test_nextGreatestLetter_6():
    letters = ["c", "f", "j"]
    target = "k"
    assert(Solution().nextGreatestLetter(letters, target) == "c")
