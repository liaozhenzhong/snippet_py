import multiprocessing as mp
import time


def worker(l):
    with l:
        print(mp.current_process().name)
        time.sleep(1)


def main():
    l = mp.Lock()
    for _ in range(4):
        mp.Process(target=worker, args=(l, )).start()


if __name__ == '__main__':
    main()
