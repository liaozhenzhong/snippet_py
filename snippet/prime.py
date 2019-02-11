def prime_factor(x):
    res = []
    end = x // 2 + 1
    for i in range(2, end):
        while x % i == 0:
            res.append(i)
            x //= i
    return res if res else [x]
