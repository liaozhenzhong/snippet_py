class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> 'bool':
        stack = []
        stack_set = set()
        pushed.reverse()
        pushed_set = set(pushed)
        for i in popped:
            if i in pushed_set:
                while True:
                    j = pushed.pop()
                    pushed_set.remove(j)
                    stack.append(j)
                    stack_set.add(j)
                    if j == i:
                        break
            elif i in stack_set:
                while True:
                    j = stack.pop()
                    stack_set.remove(j)
                    if j == i:
                        break
            else:
                return False
        return not pushed

def test_validate_stack_sequence():
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    assert Solution().validateStackSequences(pushed, popped) == True

def test_validate_stack_sequence_2():
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    assert Solution().validateStackSequences(pushed, popped) == False

def test_validate_stack_sequence_3():
    pushed = []
    popped = []
    assert Solution().validateStackSequences(pushed, popped) == True

def test_validate_stack_sequence_4():
    pushed = [1]
    popped = []
    assert Solution().validateStackSequences(pushed, popped) == False

def test_validate_stack_sequence_5():
    pushed = []
    popped = [1]
    assert Solution().validateStackSequences(pushed, popped) == False

def test_validate_stack_sequence_6():
    pushed = [0]
    popped = [1]
    assert Solution().validateStackSequences(pushed, popped) == False

def test_validate_stack_sequence_7():
    pushed = [1]
    popped = [1]
    assert Solution().validateStackSequences(pushed, popped) == True

test_validate_stack_sequence()
