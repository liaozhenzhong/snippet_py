import threading as th


l = th.RLock()


def worker():
    # with l:
    #     print(th.current_thread().name)

    l.acquire()
    print(th.current_thread().name)

    l.acquire()         # <<--- it will block unless using RLock
    print(th.current_thread().name)

    l.release()


def main():
    p = th.Thread(target=worker)
    p.start()


if __name__ == '__main__':
    main()
