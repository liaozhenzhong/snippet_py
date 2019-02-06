from snippet.reg import *

def test_regular():
    assert(match('bbc', 'a.c') == False)
    assert(match('abc', 'a.c') == True)
    assert(match('abbc', 'a.c') == False)
    assert(match('abbc', 'a..c') == True)
    assert(match('abbc', 'a...c') == False)
    assert(match('abbc', 'a*c') == False)
    assert(match('ac', 'a*c') == True)
    assert(match('aac', 'a*c') == True)
    assert(match('c', 'a*c') == True)

    assert(match('abbc', 'a.*c') == True)
    assert(match('abbhbbcf', 'a.*c') == False)
    assert(match('abbhbbbc', 'a.*c') == True)
    assert(match('', '') == True)
    assert(match('asdf', '') == False)
