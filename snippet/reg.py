def match(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        if j + 1 < len(b) and b[j+1] == '*':
            if b[j] == '*':
                return False
            elif b[j] == '.':
                for k in reversed(range(i, len(a))):
                    if match(a[k:], b[j+2:]):
                        return True
                return False
            else:
                while i < len(a) and a[i] == b[j]:
                    i += 1
                j += 2
        else:
            if b[j] == '*':
                return False
            elif b[j] == '.':
                i += 1
                j += 1
            else:
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    return False
    if i != len(a) or j != len(b):
        return False
    return True
