import threading as th


def worker(cv):
    while True:
        with cv:
            cv.wait()
            print(th.current_thread().name)


def main():
    cv = th.Condition()

    for _ in range(3):
        t = th.Thread(target=worker, args=(cv,))
        t.setDaemon(True)
        t.start()

    inp = ''
    while inp != 'q':
        inp = input()
        with cv:
            cv.notify_all()


if __name__ == '__main__':
    main()
