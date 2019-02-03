import threading as th
import time


def worker(sf):
    # sf.acquire()
    # print(th.current_thread().name, time.time())
    # time.sleep(1)
    # sf.release()

    with sf:
        print(th.current_thread().name, time.time())
        time.sleep(1)


def main():
    sf = th.Semaphore(3)
    for _ in range(7):
        th.Thread(target=worker, args=(sf, )).start()


if __name__ == '__main__':
    main()
