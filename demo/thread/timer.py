import threading as th
import datetime


def worker():
    print(th.current_thread().name, datetime.datetime.now().second)


def main():
    print(th.current_thread().name, datetime.datetime.now().second)
    t = th.Timer(1, worker)
    t.start()


if __name__ == '__main__':
    main()
