def verify(mat):
    standard = 0

    for i in range(1, 10):
        standard += 2**i

    for i in range(9):
        ver = standard
        hor = standard
        for j in range(9):
            ver -= 2**mat[i][j]
            hor -= 2**mat[j][i]
        if ver != 0:
            return False
        if hor != 0:
            return False

    for i in range(3):
        for j in range(3):
            I = 3*i + 1
            J = 3*j + 1
            box = standard
            for ii in range(I-1, I+2):
                for jj in range(J-1, J+2):
                    box -= 2**mat[ii][jj]
            if box != 0:
                return False

    return True


def test_verify():
    mat = [
            [5, 1, 7, 6, 9, 8, 2, 3, 4],
            [2, 8, 9, 1, 3, 4, 7, 5, 6],
            [3, 4, 6, 2, 7, 5, 8, 9, 1],
            [6, 7, 2, 8, 4, 9, 3, 1, 5],
            [1, 3, 8, 5, 2, 6, 9, 4, 7],
            [9, 5, 4, 7, 1, 3, 6, 8, 2],
            [4, 9, 5, 3, 6, 2, 1, 7, 8],
            [7, 2, 3, 4, 8, 1, 5, 6, 9],
            [8, 6, 1, 9, 5, 7, 4, 2, 3]]
    assert(verify(mat) == True)
    mat[0][0] = 6
    assert(verify(mat) == False)

