from random import randint
from math import inf

def k_smallest(X, k):
    res = [inf]*(k + 1)
    for x in X:
        res[-1] = x
        for i in reversed(range(len(res) - 1)):
            if res[i] > res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
    return res[:-1]

def N_house_K_color_min_cost(price_list):
    lowest_price_list = [[None for _ in range(K)] for _ in range(N)]
    lowest_price_list[0] = price_list[0]
    for i in range(1, N):
        lowest, lowest_2nd = k_smallest(lowest_price_list[i - 1], 2)
        for j in range(K):
            if price_list[i - 1][j] == lowest:
                lowest_price_list[i][j] = lowest_2nd + price_list[i][j]
            else:
                lowest_price_list[i][j] = lowest + price_list[i][j]

    return min(lowest_price_list[-1])


if __name__ == '__main__':
    # for _ in range(100):
    K = 4
    N = 4
    # price_list = [[randint(1, 10) for _ in range(K)] for _ in range(N)]
    price_list = [
        [3, 10, 2, 4],
        [6, 10, 10, 6],
        [3, 5, 4, 8],
        [2, 9, 6, 3],
    ]
    for row in price_list:
        print(row)

    res1 = N_house_K_color_min_cost(price_list)
    assert res1 == 13
    print(res1)

