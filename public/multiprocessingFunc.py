from multiprocessing import Process, cpu_count, process
import time

def counter(n):
    count = 0
    while count < n:
        count += 1

def main():
    print(cpu_count())
    a = Process(target=counter, args=(250_000_000,))
    # a.start()
    b = Process(target=counter, args=(250_000_000,))
    # b.start()
    c = Process(target=counter, args=(250_000_000,))
    # c.start()
    d = Process(target=counter, args=(250_000_000,))
    # d.start()
    # a.join()
    # b.join()
    # c.join()
    # d.join()
    print("finished in ",time.perf_counter(),"sec")
    pass

if __name__ == '__main__':
    main()