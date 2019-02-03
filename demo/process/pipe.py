import multiprocessing as mp
import time


def worker(child_conn):
    for i in range(5):
        child_conn.send(i)
        time.sleep(0.1)

    child_conn.close()


def main():
    parent_conn, child_conn = mp.Pipe()
    p = mp.Process(target=worker, args=(child_conn, ))
    p.start()

    for _ in range(10):
        if parent_conn.poll():
            print(parent_conn.recv())
        time.sleep(0.1)

    parent_conn.close()


if __name__ == '__main__':
    main()
