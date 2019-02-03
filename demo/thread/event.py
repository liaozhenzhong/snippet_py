import threading as th
import time


def worker(e):
    e.wait()
    print(th.current_thread().name)


def main():
    e = th.Event()
    print(th.current_thread().name, e.is_set())

    p = th.Thread(target=worker, args=(e, ))
    p.start()

    input()
    e.set()

    print(th.current_thread().name, e.is_set())

    time.sleep(1)
    e.clear()
    print(th.current_thread().name, e.is_set())


if __name__ == '__main__':
    main()
