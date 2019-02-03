import multiprocessing as mp


def worker(arr, val, que):
    for i in range(len(arr)):
        arr[i] = i
        que.put(-i)

    val = 2


def main():
    arr = mp.Array('i', 5)
    val = mp.Value('d', 0.0)
    que = mp.Queue()
    p = mp.Process(target=worker, args=(arr, val, que))
    p.start()
    p.join()

    print(list(arr))
    print(val.value)
    while not que.empty():
        print(que.get())


if __name__ == '__main__':
    main()
