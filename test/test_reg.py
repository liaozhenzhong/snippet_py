from snippet.reg import match

def test_regular():
    assert(match('bbc', 'a.c') == False)

def test_regular_2():
    assert(match('abc', 'a.c') == True)

def test_regular_3():
    assert(match('abbc', 'a.c') == False)

def test_regular_4():
    assert(match('abbc', 'a..c') == True)

def test_regular_5():
    assert(match('abbc', 'a...c') == False)

def test_regular_6():
    assert(match('abbc', 'a*c') == False)

def test_regular_7():
    assert(match('ac', 'a*c') == True)

def test_regular_8():
    assert(match('aac', 'a*c') == True)

def test_regular_9():
    assert(match('c', 'a*c') == True)

def test_regular_10():
    assert(match('abbc', 'a.*c') == True)

def test_regular_11():
    assert(match('abbhbbcf', 'a.*c') == False)

def test_regular_12():
    assert(match('abbhbbbc', 'a.*c') == True)

def test_regular_13():
    assert(match('', '') == True)

def test_regular_14():
    assert(match('asdf', '') == False)

def test_regular_15():
    assert(match('ab', '.*') == True)

def test_regular_16():
    assert(match('aaa', 'a*a') == True)

def test_regular_17():
    assert(match('aa', 'a*') == True)

def test_regular_18():
    assert(match('abcd', 'd*') == False)

def test_regular_19():
    assert(match('a', 'ab*') == True)

def test_regular_20():
    assert(match('abbc', 'a.*') == True)
    assert(match('abbc', 'a..*') == True)
    assert(match('abbc', 'a...*') == True)
    assert(match('abbc', 'a....*') == True)
    assert(match('abbc', 'a.....*') == False)

def test_regular_21():
    assert(match('', 'c*c*') == True)

