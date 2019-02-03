import multiprocessing as mp
import time
import random


def worker(i):
    print(mp.current_process().name.split('-')[-1], i)
    time.sleep(random.randint(1, 1000)/1000)
    for x in range(10000):
        for y in range(10000):
            z = x * y
    return i ** 2


def main():
    L = [i for i in range(100)]
    with mp.Pool(mp.cpu_count()) as p:
        # print(p.map(worker, L))     # return [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        print([i for i in p.imap_unordered(worker, L)])     # return [4, 16, 0, 9, 25, 1, 36, 49, 81, 64]


if __name__ == '__main__':
    main()
